#!/usr/bin/python
# This script contains different utilities that can be handy when dealing with lists

# Simple method that just prints the content of a list
def print_list(list_to_print):
    if isinstance(list_to_print, list):
        for e in list_to_print:
            print(e)
    else:
        print("[-] print_list method did not receive a list")


# Finds all occurrences of a substring in a list
def find_all_matches(substring, search_list):
    matches = [s for s in search_list if substring in s]
    return matches
