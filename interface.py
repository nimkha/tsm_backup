#!/usr/bin/python
# This script is creates the command line interface

import argparse
import sys
import main

# Initialize parser
parser = argparse.ArgumentParser(description="Backup Troubleshooter")

# Add optional arguments
parser.add_argument("--schedule", help="Searches for all successful and un-successful backup runs", action="store_true")
parser.add_argument("--retries", help="Searches for how many times a backup has tried to complete the run", action="store_true")
parser.add_argument("--elapsedTime", help="Returns how long it has taken to complete earlier backups", action="store_true")
parser.add_argument("--errorLog", help="Analyses the error log file", action="store_true")

# Handle arguments
args = parser.parse_args()

if args.schedule:
    print("Choose backup schedule")
    print("[1] DAILY-2100")
    print("[2] DAILY-2300")
    schedule_type = input("Option:")
    if schedule_type == "1":
        main.get_scheduled_runs("DAILY-2100")
    elif schedule_type == "2":
        main.get_scheduled_runs("DAILY-2300")
    else:
        sys.exit("[-] Did not receive a valid option, choose the number corresponding to the schedule")

if args.retries:
    main.get_total_number_of_retries()

if args.elapsedTime:
    main.get_elapsed_time_to_run_backup()

if args.errorLog:
    main.error_log_analysis()
