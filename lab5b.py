#!/usr/bin/env python3
# Author ID: msingh869

# same functions from lab5a.py
def read_file_string(file_name):
    # Takes a file name as string and returns its entire contents as a string
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    # Takes a file name as string and returns its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()

    list_of_lines = []
    for line in lines:
        list_of_lines.append(line.rstrip('\n'))
    return list_of_lines

# --- Writing/appending functions ---
def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a file name and a list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Reads data from first file, writes it to second file, adding line numbers
    f_read = open(file_name_read, 'r')
    lines = f_read.readlines()
    f_read.close()

    f_write = open(file_name_write, 'w')
    line_number = 1
    for line in lines:
        f_write.write(str(line_number) + ':' + line)
        line_number += 1
    f_write.close()

# --- Main block ---
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'

    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
