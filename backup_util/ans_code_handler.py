#!/usr/bin/python
# This script handles the error log file and analyses the different ANS codes.

import os
import re
import subprocess
import sys
from file_handler import content_manipulator as content_man
from miscellaneous_utilities import list_util


# Gathers all the ANS error lines from the error file
def ans_codes():
    path = get_error_log_path()
    print("[+] Gathering all ANS error lines...")
    try:
        result = subprocess.check_output(["grep", "ANS", path])
        new_result = content_man.string_to_list(result)
        return new_result
    except:
        sys.exit("[-] Unknown error detected in function 'ans_codes()'")


# Return a valid path for the error log
def get_error_log_path():
    print("[+] Locating error log file...")
    path1 = "/var/log/tsm/error.log"
    path2 = "/var/log/tsm/dsmerror.log"

    if os.path.exists(path1):
        print("[+] Found file at " + path1)
        return path1
    elif os.path.exists(path2):
        print("[+] Found file at " + path2)
        return path2
    else:
        sys.exit("[-] Could not find error log file")


# Filters out just the ANS code from a string
def filter_ans_code(string):
    search_result = ""
    if len(string) > 1:
        search_result = re.search(r"ANS\w\w\w\w\w", string)

    if search_result:
        return search_result.group(0)
    else:
        return False


# Removes duplicate ans code from a list from error log file.
# This is purely determined by the ANS code. Rememeber even though the ANS code is the same, the content of the code might not be
def remove_duplicate_ans_code(list_with_duplicates):
    new_list = []
    for i in list_with_duplicates:
        ans_code = filter_ans_code(i)
        if ans_code:
            bool_value = any(ans_code in s for s in new_list)
            if not bool_value:
                new_list.append(i)
    return new_list


# Gives a list of just the ANS codes without duplicates.
# Takes the complete list of error.log and removes duplicates ANS codes and then filters just the single code from the string
# and adds the content to a new list.
def list_all_ans_codes(ans_list):
    ans_codes_without_duplicates = remove_duplicate_ans_code(ans_list)
    ans_code_list = []
    for code in ans_codes_without_duplicates:
        result = filter_ans_code(code)
        ans_code_list.append(result)

    return ans_code_list


# Count all the occurrences of an ANS code
def count_all_ans_code(ans_codes):
    all_ans_codes = list_all_ans_codes(ans_codes)
    ans_dict = {}
    for i in all_ans_codes:
        hits = list_util.find_all_matches(i, ans_codes)
        ans_dict[i] = len(hits)

    result_list = []
    for x, y in ans_dict.items():
        result_list.append(x + " occurred " + str(y) + " number of times in error log file")

    return result_list


# Gathers all the ANS codes from EKB
def get_ekb_ans_codes():
    non_issue_errors = content_man.get_file_content("non_issue_error_log_entries.txt")
    valid_errors = content_man.get_file_content("ans_codes_in_ekb.txt")
    ekb_list_of_errors = non_issue_errors + valid_errors

    return ekb_list_of_errors


# Checks if ANS code is in EKB
def crosscheck_ans_codes(ans_codes):
    print("[+] Searching for error codes in EKB...")
    all_ans_codes = list_all_ans_codes(ans_codes)
    ans_codes_in_ekb = content_man.get_file_content("ans_codes_in_ekb.txt")
    non_issue_error_codes = content_man.get_file_content("non_issue_error_log_entries.txt")
    ans_found_in_ekb = []

    for ans in all_ans_codes:
        if ans in ans_codes_in_ekb:
            ans_found_in_ekb.append(ans + " Found in EKB, this error has a runbook on how to proceed")
        elif ans in non_issue_error_codes:
            ans_codes_in_ekb.append(ans + " Found in EKB, but this is a non issue error")

    return ans_found_in_ekb






