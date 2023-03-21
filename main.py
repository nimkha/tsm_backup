#!/usr/bin/python

import backup_util
import miscellaneous_utilities.list_util
from file_handler import content_manipulator
from backup_util import ans_code_handler
from backup_util import backup
from miscellaneous_utilities import list_util
import os


# Gets schedule runs, prints them to console, and adds the result to clipboard
def get_scheduled_runs(schedule):
    schedule_type = ""
    if schedule == "DAILY-2100":
        schedule_type = "Scheduled event 'DAILY-2100'"
    elif schedule == "DAILY-2300":
        schedule_type = "Scheduled event 'DAILY-2300'"

    result = backup.scheduled_run(schedule_type)
    backup.organize_search_result(result)


# Prints the time used to complete a backup and adds the result to clipboard
def get_elapsed_time_to_run_backup():
    result = backup.elapsed_time()
    backup.organize_search_result(result)


# Prints the total number of retries the backup has tried to complete the process
def get_total_number_of_retries():
    result = backup.retries()
    backup.organize_search_result(result)


# Analyzes the error log and output some basic information
def error_log_analysis():
    ans_codes_lines = ans_code_handler.ans_codes()
    print("[+] Total number of ANS lines: " + str(len(ans_codes_lines)))
    ans_no_duplicate_codes = ans_code_handler.remove_duplicate_ans_code(content_manipulator.reverse_list(ans_codes_lines))
    print()

    print("These are the latest ANS codes (without duplicates). Remember that even though the ANS code is the same the content might be different.")
    print("Manually check the error log for more in dept analysis about the content of every ANS code.\n")
    list_util.print_list(ans_no_duplicate_codes)
    print()

    number_of_ans_codes = ans_code_handler.count_all_ans_code(ans_codes_lines)
    list_util.print_list(number_of_ans_codes)

    print()
    ans_codes_in_ekb = ans_code_handler.crosscheck_ans_codes(ans_codes_lines)
    print()
    list_util.print_list(ans_codes_in_ekb)
    if len(ans_codes_lines) > 0:
        print("You can find more information on how to handle this in EKB")
        print("EKB URL")
    else:
        print("None of the ANS codes where found in EKB. Try searching manually with marve")


if __name__ == '__main__':

    # get_elapsed_time_to_run_backup()
    # get_scheduled_runs("DAILY-2100")
    # get_total_number_of_retries()
    error_log_analysis()




















