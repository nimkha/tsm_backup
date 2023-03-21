#!/usr/bin/python

# This script contains different tools to aid troubleshooting backup issues
import subprocess
import file_handler.content_manipulator as content_man
import sys
import miscellaneous_utilities.list_util

# Outputs all the successful and unsuccessful backups that are logged in the schedule log file
def scheduled_run(schedule):
    path = get_schedule_log_path()
    print("[+] Gathering all successful and un-successful backup runs")
    try:
        result = subprocess.check_output(["grep", schedule, path])
        return result
    except:
        sys.exit("[-] No scheduled runs found for " + schedule)


# Outputs the elapsed time it has taken to complete a backup.
# This is good to know for when you are running manual backup.
def elapsed_time():
    path = get_schedule_log_path()
    print("[+] Searching for how a long it has taken to complete a backup...")
    try:
        result = subprocess.check_output(["grep", "Elapsed", path])
        return result
    except:
        sys.exit("[-] Unknown error detected in function 'elapsed_time()'")


# Outputs total number of retries a backup has attempted
def retries():
    path = get_schedule_log_path()
    print("[+] Searching for number of backup execution retries...")
    try:
        result = subprocess.check_output(["grep", "Total number of retries:", path])
        return result
    except:
        sys.exit("[-] Unknown error detected in function 'retries()'")


# Returns a valid path for the schedule log
def get_schedule_log_path():
    print("[+] Locating schedule log file...")
    path1 = "/var/log/tsm/sched.log"
    path2 = "/var/log/tsm/schederror.log"
    path3 = "/var/log/tsm/dsmsched.log"

    if content_man.does_file_exist(path1):
        print("[+] Found file at " + path1)
        return path1
    elif content_man.does_file_exist(path2):
        print("[+] Found file at " + path2)
        return path2
    elif content_man.does_file_exist(path3):
        print("[+] Found file at " + path3)
        return path3
    else:
        sys.exit("[-] Could not find schedule log file")


# Organizes search result, prints out the result, and add content to clipboard.
# Use this for instance in together with the elapsed time and retries method.
def organize_search_result(result):
    list_results = content_man.string_to_list(result)
    print()
    miscellaneous_utilities.list_util.print_list(list_results)
    content_man.add_list_to_clipboard(list_results)
    print("[+] Content added to clipboard")












