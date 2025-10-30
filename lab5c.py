#!/usr/bin/env python3
# Author ID: msingh869

# --- Add two numbers together, handling exceptions ---
def add(number1, number2):
    # Add two numbers together, return the result
    # If there is an error, return string 'error: could not add numbers'
    try:
        return int(number1) + int(number2)
    except:
        return 'error: could not add numbers'

# --- Read a file, handling exceptions ---
def read_file(filename):
    # Read a file, return a list of all lines
    # If there is an error, return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except:
        return 'error: could not read file'

# --- Main block ---
if __name__ == '__main__':
    # Test the add function
    print(add(10, 5))       # works
    print(add('10', 5))     # works
    print(add('abc', 5))    # exception

    # Test the read_file function
    print(read_file('seneca2.txt'))     # works
    print(read_file('file10000.txt'))   # exception
