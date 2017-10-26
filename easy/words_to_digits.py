#!usr/bin/env python3
"""
Words To Digits
Solution Author: Mild Z Ferdinand
Description:
     Having a string representation of a set of numbers you need to print this
     numbers. All numbers are separated by semicolon. There are up to 20
     numbers in one line. The numbers are "zero" to "nine"
"""
import sys


WORD_MAP = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    }


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            word_numbers = line.strip().split(';')
            nums = (str(WORD_MAP[i]) for i in word_numbers)
            print("".join(nums))


if __name__ == "__main__":
    main()