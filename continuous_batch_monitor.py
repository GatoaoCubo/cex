#!/usr/bin/env python3
"""
Continuous Batch Monitor for CRM Expansion Operations
Tracks parallel nucleus execution and coordinates completion.
"""

import time
import json
from pathlib import Path
from datetime import datetime
import subprocess

def check_nucleus_status():
    """Check current status of running nuclei."""
    try:
        result = subprocess.run(
            ["bash", "_spawn/dispatch.sh", "status"],
            capture_output=True,
            text=True,
            cwd="C:/Users/PC/Documents/GitHub/cex"
        )
        return result.stdout
    except Exception as e:
        print(f"Error checking status: {e}")
        return ""

def check_signals():
    """Check for completion signals from nuclei."""
    signals_dir = Path("C:/Users/PC/Documents/GitHub/cex/.cex/runtime/signals")
    if not signals_dir.exists():
        return {}

    signals = {}
    for signal_file in signals_dir.glob("*.json"):
        try:
            with open(signal_file, 'r') as f:
                data = json.load(f)
                signals[signal_file.stem] = data
        except Exception as e:
            print(f"Error reading signal {signal_file}: {e}")

    return signals

def check_git_commits():
    """Check for new commits indicating work completion."""
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "-10"],
            capture_output=True,
            text=True,
            cwd="C:/Users/PC/Documents/GitHub/cex"
        )
        return result.stdout.split('\n')[:5]  # Last 5 commits
    except Exception as e:
        print(f"Error checking git: {e}")
        return []

def check_new_files():
    """Check for new files created by nuclei."""
    target_dirs = [
        "N01_intelligence",
        "N02_marketing",
        "N03_builder",
        "N06_commercial",
        "N01_research/output"
    ]

    new_files = {}
    for dir_name in target_dirs:
        dir_path = Path(f"C:/Users/PC/Documents/GitHub/cex/{dir_name}")
        if dir_path.exists():
            files = list(dir_path.glob("**/*.md"))
            # Get files modified in last 30 minutes
            recent_files = []
            cutoff = time.time() - 1800  # 30 minutes
            for f in files:
                if f.stat().st_mtime > cutoff:
                    recent_files.append(f.name)
            if recent_files:
                new_files[dir_name] = recent_files

    return new_files

def main():
    """Main monitoring loop."""
    print("🔄 Continuous Batch Monitor - CRM Expansion Operations")
    print("=" * 60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")

    start_time = time.time()
    last_status_check = 0
    check_interval = 60  # Check every minute

    completed_nuclei = set()

    while True:
        current_time = time.time()

        # Status check every minute
        if current_time - last_status_check > check_interval:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Status Check")
            print("-" * 30)

            # Check nucleus status
            status = check_nucleus_status()
            if status:
                print("Nucleus Status:")
                print(status)

            # Check for signals
            signals = check_signals()
            if signals:
                print(f"Signals detected: {len(signals)}")
                for nucleus, signal_data in signals.items():
                    if nucleus not in completed_nuclei:
                        print(f"  ✅ {nucleus}: {signal_data.get('status', 'completed')}")
                        completed_nuclei.add(nucleus)

            # Check for new commits
            commits = check_git_commits()
            if commits:
                print("Recent commits:")
                for commit in commits:
                    if commit.strip():
                        print(f"  {commit}")

            # Check for new files
            new_files = check_new_files()
            if new_files:
                print("New files created:")
                for directory, files in new_files.items():
                    print(f"  {directory}: {', '.join(files)}")

            # Calculate runtime
            runtime = (current_time - start_time) / 60
            print(f"Runtime: {runtime:.1f} minutes")

            last_status_check = current_time

        # Check if all nuclei completed
        expected_nuclei = {"n01_quality", "n01_expansion", "n02_outreach", "n03_automation", "n06_sales"}
        if len(completed_nuclei) >= 3:  # At least 3 major deliverables
            print("\n🎯 MAJOR DELIVERABLES COMPLETED!")
            print(f"Completed nuclei: {completed_nuclei}")
            break

        # Safety timeout after 2 hours
        if runtime > 120:
            print("\n⏰ TIMEOUT: 2 hours elapsed, stopping monitor")
            break

        time.sleep(30)  # Check every 30 seconds

    # Final summary
    print("\n" + "=" * 60)
    print("🔥 CONTINUOUS BATCH EXECUTION SUMMARY")
    print(f"Total runtime: {(time.time() - start_time) / 60:.1f} minutes")
    print(f"Completed nuclei: {len(completed_nuclei)}")
    print(f"Final signals: {list(completed_nuclei)}")

    # Check final deliverables
    final_files = check_new_files()
    if final_files:
        print("\nFinal deliverables:")
        for directory, files in final_files.items():
            for file in files:
                print(f"  📄 {directory}/{file}")

    print("\n✅ Continuous batching monitoring complete!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ Monitor stopped by user")
    except Exception as e:
        print(f"\n❌ Monitor error: {e}")