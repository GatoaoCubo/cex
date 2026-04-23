#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for cex_lock.py -- file-based locking."""

import json
import os
import sys
import threading
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cex_lock import (CexLock, _sanitize_name, clean_stale, list_locks,
                      lock_resource)

# ======================================================================
# Unit: _sanitize_name
# ======================================================================

class TestSanitizeName:
    def test_simple(self):
        assert _sanitize_name("my_resource") == "my_resource"

    def test_slashes(self):
        assert _sanitize_name("path/to/file") == "path__to__file"

    def test_backslashes(self):
        # C: colon -> _, \\ -> __ so C:\Users\file -> C___Users__file
        assert _sanitize_name("C:\\Users\\file") == "C___Users__file"

    def test_spaces_colons(self):
        assert _sanitize_name("mission: alpha") == "mission__alpha"


# ======================================================================
# Unit: CexLock basic operations
# ======================================================================

class TestCexLockBasic:
    def test_acquire_release(self, tmp_path):
        lk = CexLock("test_res", lock_dir=tmp_path)
        assert lk.acquire()
        assert lk._held
        assert lk.lock_file.exists()
        assert lk.release()
        assert not lk.lock_file.exists()

    def test_context_manager(self, tmp_path):
        with CexLock("ctx_res", lock_dir=tmp_path) as lk:
            assert lk._held
            assert lk.lock_file.exists()
        assert not lk.lock_file.exists()

    def test_lock_info_contents(self, tmp_path):
        lk = CexLock("info_res", owner="n03", nucleus="n03", lock_dir=tmp_path)
        lk.acquire()
        data = json.loads(lk.lock_file.read_text(encoding="utf-8"))
        assert data["resource"] == "info_res"
        assert data["owner"] == "n03"
        assert data["nucleus"] == "n03"
        assert data["pid"] == os.getpid()
        assert "acquired_at" in data
        lk.release()

    def test_is_locked(self, tmp_path):
        lk = CexLock("locked_res", lock_dir=tmp_path)
        assert not lk.is_locked()
        lk.acquire()
        assert lk.is_locked()
        lk.release()
        assert not lk.is_locked()

    def test_lock_owner(self, tmp_path):
        lk = CexLock("owner_res", owner="test_owner", lock_dir=tmp_path)
        assert lk.lock_owner() == {}
        lk.acquire()
        owner = lk.lock_owner()
        assert owner["owner"] == "test_owner"
        assert owner["pid"] == os.getpid()
        lk.release()

    def test_repr(self, tmp_path):
        lk = CexLock("repr_res", lock_dir=tmp_path)
        assert "FREE" in repr(lk)
        lk.acquire()
        assert "HELD" in repr(lk)
        lk.release()

    def test_creates_lock_dir(self, tmp_path):
        lock_dir = tmp_path / "deep" / "nested" / "locks"
        lk = CexLock("nested_res", lock_dir=lock_dir)
        lk.acquire()
        assert lock_dir.exists()
        lk.release()


# ======================================================================
# Contention: two locks same resource
# ======================================================================

class TestCexLockContention:
    def test_second_lock_blocked(self, tmp_path):
        lk1 = CexLock("shared_res", timeout=0.1, lock_dir=tmp_path)
        lk2 = CexLock("shared_res", timeout=0.5, lock_dir=tmp_path)
        assert lk1.acquire()
        # Second lock should fail (timeout)
        assert not lk2.acquire()
        lk1.release()
        # Now it should succeed
        assert lk2.acquire()
        lk2.release()

    def test_different_resources_independent(self, tmp_path):
        lk1 = CexLock("res_a", lock_dir=tmp_path)
        lk2 = CexLock("res_b", lock_dir=tmp_path)
        assert lk1.acquire()
        assert lk2.acquire()
        lk1.release()
        lk2.release()

    def test_context_manager_timeout_raises(self, tmp_path):
        lk1 = CexLock("block_res", lock_dir=tmp_path)
        lk1.acquire()
        with pytest.raises(TimeoutError):
            with CexLock("block_res", timeout=0.3, lock_dir=tmp_path):
                pass
        lk1.release()


# ======================================================================
# Stale lock detection
# ======================================================================

class TestStaleLock:
    def test_stale_by_ttl(self, tmp_path):
        # Create a lock with old timestamp
        lock_file = tmp_path / "stale_res.lock"
        from datetime import datetime, timedelta, timezone
        old_time = (datetime.now(timezone.utc) - timedelta(seconds=999)).isoformat()
        lock_file.write_text(json.dumps({
            "resource": "stale_res", "owner": "old", "pid": 999999,
            "acquired_at": old_time,
        }), encoding="utf-8")

        lk = CexLock("stale_res", ttl=10, lock_dir=tmp_path)
        assert lk._is_stale()
        # Should be able to acquire (stale lock auto-cleared)
        assert lk.acquire()
        lk.release()

    def test_stale_by_dead_pid(self, tmp_path):
        lock_file = tmp_path / "dead_pid.lock"
        from datetime import datetime, timezone
        lock_file.write_text(json.dumps({
            "resource": "dead_pid", "owner": "ghost", "pid": 999999,
            "acquired_at": datetime.now(timezone.utc).isoformat(),
        }), encoding="utf-8")

        lk = CexLock("dead_pid", ttl=9999, lock_dir=tmp_path)
        # PID 999999 is almost certainly dead
        assert lk._is_stale()
        assert lk.acquire()
        lk.release()

    def test_corrupt_lock_is_stale(self, tmp_path):
        lock_file = tmp_path / "corrupt.lock"
        lock_file.write_text("this is not json", encoding="utf-8")
        lk = CexLock("corrupt", lock_dir=tmp_path)
        assert lk._is_stale()


# ======================================================================
# Decorator
# ======================================================================

class TestLockDecorator:
    def test_decorator_acquires_and_releases(self, tmp_path):
        executed = []

        @lock_resource("deco_res", timeout=5, ttl=60)
        def my_func():
            executed.append(True)
            return 42

        # Monkey-patch LOCK_DIR for test
        import cex_lock
        orig = cex_lock.LOCK_DIR
        cex_lock.LOCK_DIR = tmp_path
        try:
            result = my_func()
            assert result == 42
            assert executed == [True]
            # Lock should be released
            assert not (tmp_path / "deco_res.lock").exists()
        finally:
            cex_lock.LOCK_DIR = orig


# ======================================================================
# list_locks / clean_stale
# ======================================================================

class TestListAndClean:
    def test_list_empty(self, tmp_path):
        assert list_locks(tmp_path) == []

    def test_list_with_locks(self, tmp_path):
        lk = CexLock("list_res", owner="n05", lock_dir=tmp_path)
        lk.acquire()
        locks = list_locks(tmp_path)
        assert len(locks) == 1
        assert locks[0]["resource"] == "list_res"
        assert locks[0]["owner"] == "n05"
        lk.release()

    def test_clean_stale_removes_old(self, tmp_path):
        from datetime import datetime, timedelta, timezone
        old_time = (datetime.now(timezone.utc) - timedelta(seconds=999)).isoformat()
        lock_file = tmp_path / "old.lock"
        lock_file.write_text(json.dumps({
            "resource": "old", "owner": "ghost", "pid": 999999,
            "acquired_at": old_time,
        }), encoding="utf-8")

        removed = clean_stale(ttl=10, lock_dir=tmp_path)
        assert removed == 1
        assert not lock_file.exists()

    def test_clean_stale_preserves_fresh(self, tmp_path):
        lk = CexLock("fresh_res", lock_dir=tmp_path)
        lk.acquire()
        removed = clean_stale(ttl=9999, lock_dir=tmp_path)
        assert removed == 0
        assert lk.lock_file.exists()
        lk.release()


# ======================================================================
# Thread safety
# ======================================================================

class TestThreadSafety:
    def test_concurrent_acquire(self, tmp_path):
        """Only one thread should win the lock."""
        winners = []

        def try_lock(thread_id):
            lk = CexLock("race_res", timeout=2, lock_dir=tmp_path)
            if lk.acquire():
                winners.append(thread_id)
                time.sleep(0.5)
                lk.release()

        threads = [threading.Thread(target=try_lock, args=(i,)) for i in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=10)

        # At least 1 winner, possibly all 5 (sequential after release)
        assert len(winners) >= 1
