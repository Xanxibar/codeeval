#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Swap Case

Challenge Description:

Write a program which swaps letters' case in a sentence. All non-letter
characters should remain the same.
"""
import sys

input_file = sys.argv[1]


def main():
    with open(input_file, 'r') as text:
        for line in text:
            mystring = line.strip()
            print(mystring.swapcase())
    return True


if __name__ == "__main__":
    main()