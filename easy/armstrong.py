#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Description: An Armstrong number is an n-digit number that is equal to the sum
of the n'th powers of its digits. Determine if the input numbers are
Armstrong numbers. Print out True/False if the number is an Armstrong
number or not."""

import sys


def is_armstrong(nums):
    """Returns True if nums is an Armstrong number, False otherwise."""
    number = nums
    power = len(number)
    acc = []
    for i in tuple(map(int, tuple(number))):
        acc.append(i ** power)
    total = sum(acc)
    if int(number) == total:
        return True
    return False


def main():
    try:
        input_file = sys.argv[1]
    except:
        return "Please enter path of input file as a command line argument."
    with open(input_file, 'r') as text:
        for line in text:
            number = line.strip()
            print(is_armstrong(number))
    return True



if __name__ == "__main__":
    main()