#!/usr/bin/python
# This script handles different ways of manipulating text files

import sys
import pyperclip
import os


# Returns file content from a file as a list using encoding="utf-8" as default
# Be aware some files are encoded with iso-8859-15
def get_file_content(file_path):
    print("[+] Getting content from " + file_path)

    try:
        with open(file_path, "r") as f:
            file_content = [line.strip() for line in f]
        return file_content

    except (UnicodeDecodeError, FileNotFoundError) as error:
        if type(error) == UnicodeDecodeError:
            sys.exit("[-] A unicode decode error found => " + str(error))
        elif type(error) == FileNotFoundError:
            sys.exit("[-] File not found")
        else:
            sys.exit("[-] Unknown error detected => " + str(error))


# Remove duplicates from list one by one. This can also be done by using sets
def remove_duplicates(list_with_duplicates):
    print("[+] Removing duplicates...")
    new_list = []
    for i in list_with_duplicates:
        bool_value = any(i[20:] in s for s in new_list)
        if not bool_value:
            new_list.append(i)
    return new_list


# Checks if string is byte and converts to string if it is.
def convert_to_string(string):
    if isinstance(string, bytes):
        new_string = string.decode()
        return new_string
    else:
        print("[-] Could not convert byte string. Check string type.")


# Copies file content to clipboard
def add_to_clipboard(content):
    try:
        clipboard = pyperclip.copy(content)
        return clipboard
    except pyperclip.PyperclipException:
        print("[-] Pyperclip exception found in function add_to_clipboard. Only str, int, float, and bool values can be copied to the clipboard")


# Reversing the order of a list
def reverse_list(lst):
    new_lst = lst[::-1]
    return new_lst


# Checks if a file is located at the specified path.
def does_file_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False


# Converts a byte string to list
def string_to_list(byte_string):
    if isinstance(byte_string, bytes):
        string = convert_to_string(byte_string)
        new_list = string.split('\n')
        return new_list


# Converts list to string with new line characters
def list_to_string(input):
    new_string = ""
    if isinstance(input, list):
        for e in input:
            new_string += e + "\n"
    else:
        print("[-] Did not receive list as input in function list_to_string()")

    return new_string.encode("unicode_escape")


# Takes a list as input and adds the content to clipboard. This is different to just adding a single string.
def add_list_to_clipboard(input):
    pyperclip.copy("\n".join(input))














