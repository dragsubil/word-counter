#! /usr/bin/env python3

# This program takes a text or html file as input and produces a JSON string
# which is written to the specified output file.
# The JSON string contains the filename, filepath, filetype, the total and
# individual word counts.

# Run this program from the commmand line as
# $ python3 run.py <input_file> <output_file>

import wordcounter
import sys


def writetofile(filename, op_file):
    wordcount_obj = wordcounter.WordCount(filename)
    pretty_dict = wordcount_obj.get_result()
    with open(op_file, "w+") as file1:
        file1.write(pretty_dict)


if __name__ == '__main__':
    try:
        input_file = sys.argv[1]
    except:
        input_file = str(input("Enter input file path: "))
    try:
        output_file = sys.argv[2]
    except:
        output_file = str(input("Enter output file path: "))

    writetofile(input_file, output_file)
