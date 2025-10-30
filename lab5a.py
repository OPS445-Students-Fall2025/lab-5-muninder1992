#!/usr/bin/env python3
# Author ID: msingh869

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r') 
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
 f = open(file_name, 'r')       # Open file for reading
 lines = f.readlines()          # Read entire file into a list, each line as a string
 f.close()                      # Close the file
 return [line.rstrip('\n') for line in lines]  # remove newline characters


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
