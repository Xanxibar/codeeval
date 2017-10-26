#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Even Numbers

Challenge Description:

Write a program which checks input numbers and determines whether a number is
even or not. Print 1 if the number is even or 0 if the number is odd.
"""
import sys

input_file = sys.argv[1]


def is_even(input_number):
    """Returns 1 if the input number is even and 0 otherwise."""
    return (input_number + 3) % 2


def main():
    with open(input_file, 'r') as text:
        for line in text:
            number = int(line.strip())
            print(is_even(number))
    return True


if __name__ == "__main__":
    main()