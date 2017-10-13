#!usr/bin/env python3

"""
Rightmost Char
Challenge Description:

You are given a string 'S' and a character 't'. Print out the position of the
rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none. The
position to be printed out is zero based.

Solution by: Mild Z Ferdinand
"""

import sys

input_file = sys.argv[1]


def main():
    with open(input_file, 'r') as text:
        for line in text:
            sample_string, char = line.strip().split(',')
            if not sample_string:
                continue
            try:
                index = sample_string.rindex(char)
                print(index)
            except ValueError:
                print('-1')

    return True


if __name__ == "__main__":
    main()