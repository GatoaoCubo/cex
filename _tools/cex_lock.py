#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Lock Manager v1.0 -- File-based locking for nucleus coordination.

Prevents two nuclei from writing the same file or resource simultaneously.
Uses atomic file creation (os.open O_CREAT|O_EXCL) for lock acquisition.

Features:
  - Named resource locks (file paths, mission names, nucleus IDs)
  - Timeout + retry with exponential backoff
  - Stale lock detection (configurable TTL)
  - Context manager + decorator support
  - Lock owner tracking (nucleus + PID + timestamp)
  - Cross-platform (Windows + Linux)

Usage:
    from cex_lock import CexLock, lock_resource

    # Context manager
    with CexLock("n03_output.md") as lk:
        write_file(...)

    # Decorator
    @lock_resource("grid_status")
    def update_grid():
        ...

    # Manual
    lk = CexLock("mission_state", timeout=30)
    if lk.acquire():
        try:
            ...
        finally:
            lk.release()

CLI:
    python _tools/cex_lock.py --acquire my_resource --owner n03 --timeout 10
    python _tools/cex_lock.py --release my_resource
    python _tools/cex_lock.py --status
    python _tools/cex_lock.py --clean-stale --ttl 300
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK_DIR = ROOT / ".cex" / "runtime" / "locks"

# Default stale lock TTL: 5 minutes
DEFAULT_TTL = 300
DEFAULT_TIMEOUT = 30
DEFAULT_POLL = 0.2
MAX_BACKOFF = 5.0


def _sanitize_name(name: str) -> str:
    """Convert resource name to safe filename."""
    return name.replace("/", "__").replace("\\", "__").replace(":", "_").replace(" ", "_")


class CexLock:
    """File-based resource lock with atomic creation.

    Lock file contains JSON: {owner, pid, nucleus, acquired_at, resource}.
    Acquisition uses O_CREAT|O_EXCL for atomicity (no race conditions).
    """

    def __init__(
        self,
        resource: str,
        owner: str = "",
        nucleus: str = "",
        timeout: float = DEFAULT_TIMEOUT,
        ttl: float = DEFAULT_TTL,
        lock_dir: Path = LOCK_DIR,
    ):
        self.resource = resource
        self.owner = owner or os.environ.get("CEX_NUCLEUS", f"pid_{os.getpid()}")
        self.nucleus = nucleus or os.environ.get("CEX_NUCLEUS", "")
        self.timeout = timeout
        self.ttl = ttl
        self.lock_dir = Path(lock_dir)
        self.lock_file = self.lock_dir / f"{_sanitize_name(resource)}.lock"
        self._held = False

    def _lock_info(self) -> dict:
        """Build lock metadata."""
        return {
            "resource": self.resource,
            "owner": self.owner,
            "nucleus": self.nucleus,
            "pid": os.getpid(),
            "acquired_at": datetime.now(timezone.utc).isoformat(),
        }

    def _is_stale(self) -> bool:
        """Check if existing lock file is stale (older than TTL)."""
        if not self.lock_file.exists():
            return False
        try:
            data = json.loads(self.lock_file.read_text(encoding="utf-8"))
            acquired = datetime.fromisoformat(data["acquired_at"])
            age = (datetime.now(timezone.utc) - acquired).total_seconds()
            if age > self.ttl:
                return True
            # Also check if owning PID is dead
            owner_pid = data.get("pid", 0)
            if owner_pid and not _pid_alive(owner_pid):
                return True
        except (json.JSONDecodeError, KeyError, ValueError, OSError):
            # Corrupted lock file = stale
            return True
        return False

    def acquire(self) -> bool:
        """Try to acquire the lock within timeout.

        Returns True if acquired, False if timeout.
        Uses exponential backoff between retries.
        """
        self.lock_dir.mkdir(parents=True, exist_ok=True)
        start = time.monotonic()
        backoff = DEFAULT_POLL

        while True:
            # Try atomic create
            try:
                fd = os.open(
                    str(self.lock_file),
                    os.O_CREAT | os.O_EXCL | os.O_WRONLY,
                    0o644,
                )
                os.write(fd, json.dumps(self._lock_info(), indent=2).encode("utf-8"))
                os.close(fd)
                self._held = True
                return True
            except FileExistsError:
                pass
            except OSError as e:
                # On Windows, O_EXCL may raise PermissionError instead
                if "exist" in str(e).lower() or e.errno == 17:
                    pass
                else:
                    raise

            # Lock exists -- check stale
            if self._is_stale():
                try:
                    self.lock_file.unlink(missing_ok=True)
                    continue  # Retry immediately after clearing stale
                except OSError:
                    pass

            # Timeout check
            elapsed = time.monotonic() - start
            if elapsed >= self.timeout:
                return False

            # Exponential backoff
            time.sleep(min(backoff, MAX_BACKOFF, self.timeout - elapsed))
            backoff = min(backoff * 1.5, MAX_BACKOFF)

    def release(self) -> bool:
        """Release the lock. Returns True if released, False if not held."""
        if self.lock_file.exists():
            try:
                # Verify we own this lock before releasing
                data = json.loads(self.lock_file.read_text(encoding="utf-8"))
                if data.get("pid") != os.getpid() and not self._held:
                    return False  # Not our lock
            except (json.JSONDecodeError, OSError):
                pass
            try:
                self.lock_file.unlink(missing_ok=True)
                self._held = False
                return True
            except OSError:
                return False
        self._held = False
        return True

    def is_locked(self) -> bool:
        """Check if resource is currently locked (by anyone)."""
        if not self.lock_file.exists():
            return False
        if self._is_stale():
            return False
        return True

    def lock_owner(self) -> dict:
        """Get info about current lock holder. Empty dict if unlocked."""
        if not self.lock_file.exists():
            return {}
        try:
            return json.loads(self.lock_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}

    # Context manager
    def __enter__(self):
        if not self.acquire():
            raise TimeoutError(
                f"Could not acquire lock on '{self.resource}' within {self.timeout}s. "
                f"Current owner: {self.lock_owner()}"
            )
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.release()
        return False

    def __repr__(self):
        state = "HELD" if self._held else ("LOCKED" if self.is_locked() else "FREE")
        return f"CexLock('{self.resource}', state={state})"


def _pid_alive(pid: int) -> bool:
    """Check if PID is alive (cross-platform)."""
    if sys.platform == "win32":
        import subprocess
        try:
            result = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}", "/NH"],
                capture_output=True, text=True, timeout=5,
            )
            return str(pid) in result.stdout
        except Exception:
            return False
    else:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False


# ======================================================================
# Decorator
# ======================================================================

def lock_resource(resource: str, timeout: float = DEFAULT_TIMEOUT, ttl: float = DEFAULT_TTL):
    """Decorator to lock a resource during function execution.

    @lock_resource("grid_status")
    def update_grid():
        ...
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            with CexLock(resource, timeout=timeout, ttl=ttl):
                return fn(*args, **kwargs)
        return wrapper
    return decorator


# ======================================================================
# Status / Cleanup
# ======================================================================

def list_locks(lock_dir: Path = LOCK_DIR) -> list:
    """List all current locks with metadata."""
    results = []
    if not lock_dir.exists():
        return results
    for lf in sorted(lock_dir.glob("*.lock")):
        try:
            data = json.loads(lf.read_text(encoding="utf-8"))
            acquired = datetime.fromisoformat(data.get("acquired_at", ""))
            age = (datetime.now(timezone.utc) - acquired).total_seconds()
            pid = data.get("pid", 0)
            alive = _pid_alive(pid) if pid else None
            data["_age_seconds"] = round(age, 1)
            data["_pid_alive"] = alive
            data["_file"] = lf.name
            results.append(data)
        except (json.JSONDecodeError, ValueError, OSError):
            results.append({"_file": lf.name, "_error": "corrupt"})
    return results


def clean_stale(ttl: float = DEFAULT_TTL, lock_dir: Path = LOCK_DIR) -> int:
    """Remove stale locks. Returns count of removed locks."""
    removed = 0
    if not lock_dir.exists():
        return removed
    for lf in lock_dir.glob("*.lock"):
        try:
            data = json.loads(lf.read_text(encoding="utf-8"))
            acquired = datetime.fromisoformat(data.get("acquired_at", ""))
            age = (datetime.now(timezone.utc) - acquired).total_seconds()
            pid = data.get("pid", 0)
            alive = _pid_alive(pid) if pid else False
            if age > ttl or not alive:
                lf.unlink(missing_ok=True)
                removed += 1
                print(f"  Removed stale lock: {lf.name} (age={age:.0f}s, pid_alive={alive})")
        except (json.JSONDecodeError, ValueError, OSError):
            lf.unlink(missing_ok=True)
            removed += 1
    return removed


# ======================================================================
# CLI
# ======================================================================

def main():
    p = argparse.ArgumentParser(description="CEX Lock Manager")
    p.add_argument("--acquire", metavar="RESOURCE", help="Acquire a lock")
    p.add_argument("--release", metavar="RESOURCE", help="Release a lock")
    p.add_argument("--check", metavar="RESOURCE", help="Check if resource is locked")
    p.add_argument("--status", action="store_true", help="List all locks")
    p.add_argument("--clean-stale", action="store_true", help="Remove stale locks")
    p.add_argument("--owner", default="", help="Lock owner name (default: CEX_NUCLEUS env)")
    p.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help=f"Lock timeout (default: {DEFAULT_TIMEOUT}s)")
    p.add_argument("--ttl", type=float, default=DEFAULT_TTL, help=f"Stale lock TTL (default: {DEFAULT_TTL}s)")
    args = p.parse_args()

    if args.acquire:
        lk = CexLock(args.acquire, owner=args.owner, timeout=args.timeout, ttl=args.ttl)
        if lk.acquire():
            print(f"ACQUIRED: {args.acquire} (pid={os.getpid()})")
            print(f"  Lock file: {lk.lock_file}")
            print(f"  Release with: python {__file__} --release {args.acquire}")
        else:
            owner = lk.lock_owner()
            print(f"FAILED: Could not acquire '{args.acquire}' within {args.timeout}s")
            if owner:
                print(f"  Held by: {owner.get('owner')} (pid={owner.get('pid')})")
            sys.exit(1)

    elif args.release:
        lk = CexLock(args.release)
        lk._held = True  # Force release from CLI
        if lk.release():
            print(f"RELEASED: {args.release}")
        else:
            print(f"FAILED: Could not release '{args.release}'")
            sys.exit(1)

    elif args.check:
        lk = CexLock(args.check, ttl=args.ttl)
        if lk.is_locked():
            owner = lk.lock_owner()
            print(f"LOCKED: {args.check}")
            print(f"  Owner: {owner.get('owner', '?')} | PID: {owner.get('pid', '?')}")
            print(f"  Since: {owner.get('acquired_at', '?')}")
        else:
            print(f"FREE: {args.check}")

    elif args.status:
        locks = list_locks()
        if not locks:
            print("No active locks.")
        else:
            print(f"{len(locks)} active lock(s):")
            for lk in locks:
                if "_error" in lk:
                    print(f"  {lk['_file']}: CORRUPT")
                else:
                    alive = "alive" if lk.get("_pid_alive") else "DEAD"
                    print(f"  {lk['resource']}: owner={lk.get('owner')} pid={lk.get('pid')} ({alive}) age={lk.get('_age_seconds', '?')}s")

    elif args.clean_stale:
        removed = clean_stale(ttl=args.ttl)
        print(f"Cleaned {removed} stale lock(s)")

    else:
        p.print_help()


if __name__ == "__main__":
    main()
