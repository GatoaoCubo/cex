#!/usr/bin/env python3
"""
Simple Batch Monitor for CRM Expansion Operations
ASCII-only version for Windows compatibility.
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
    cutoff = time.time() - 1800  # Last 30 minutes

    for dir_name in target_dirs:
        dir_path = Path(f"C:/Users/PC/Documents/GitHub/cex/{dir_name}")
        if dir_path.exists():
            recent_files = []
            for f in dir_path.glob("**/*.md"):
                try:
                    if f.stat().st_mtime > cutoff:
                        recent_files.append(f.name)
                except:
                    pass
            if recent_files:
                new_files[dir_name] = recent_files

    return new_files

def count_running_processes():
    """Count running nucleus processes."""
    status = check_nucleus_status()
    if not status:
        return 0

    lines = status.split('\n')
    running_count = 0
    for line in lines:
        if 'RUNNING' in line:
            running_count += 1

    return running_count

def main():
    """Main monitoring loop."""
    print("CONTINUOUS BATCH MONITOR - CRM Expansion Operations")
    print("=" * 60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    print("Monitoring 4 parallel nuclei:")
    print("- N01: Business validation & market intelligence")
    print("- N02: Outreach campaigns & lead nurturing")
    print("- N03: CRM automation & management tools")
    print("- N06: Sales prioritization & revenue modeling")
    print("")

    start_time = time.time()
    last_status_check = 0
    check_interval = 90  # Check every 90 seconds

    total_deliverables = 0
    max_deliverables = 15  # Expected total deliverables

    while True:
        current_time = time.time()
        runtime = (current_time - start_time) / 60

        # Status check
        if current_time - last_status_check > check_interval:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Status Check - Runtime: {runtime:.1f}min")
            print("-" * 45)

            # Count running processes
            running = count_running_processes()
            print(f"Running nuclei: {running}")

            # Check for new deliverables
            new_files = check_new_files()
            current_deliverables = 0

            if new_files:
                print("Recent deliverables:")
                for directory, files in new_files.items():
                    current_deliverables += len(files)
                    for file in files:
                        print(f"  {directory}: {file}")

                total_deliverables = max(total_deliverables, current_deliverables)

            print(f"Total deliverables: {total_deliverables}/{max_deliverables}")
            print(f"Progress: {(total_deliverables/max_deliverables)*100:.1f}%")

            last_status_check = current_time

        # Stop conditions
        if running == 0 and runtime > 5:
            print("\nAll nuclei completed!")
            break

        if total_deliverables >= 8:  # Good progress threshold
            print("\nMajor deliverables completed!")
            break

        if runtime > 120:  # 2 hour timeout
            print("\nTimeout reached (2 hours)")
            break

        time.sleep(30)  # Check every 30 seconds

    # Final summary
    print("\n" + "=" * 60)
    print("BATCH EXECUTION SUMMARY")
    print(f"Total runtime: {runtime:.1f} minutes")
    print(f"Final deliverables: {total_deliverables}")

    # Check final status
    final_files = check_new_files()
    if final_files:
        print("\nFinal deliverables:")
        for directory, files in final_files.items():
            for file in files:
                print(f"  {directory}/{file}")

    print("\nContinuous batching monitoring complete!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitor stopped by user")
    except Exception as e:
        print(f"Monitor error: {e}")