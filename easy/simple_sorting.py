#!usr/bin/env python3
"""
Simple Sorting challenge
Solution Author: Mild Z Ferdinand
Description: Write a program which sorts numbers. Print sorted numbers in the
following way. Please note, that you need to print the numbers till the 3rd
digit after the dot including trailing zeros.
"""
import sys


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            numbers = sorted([float(i) for i in line.strip().split()])
            output_numbers = " ".join(["{:.3f}".format(i) for i in numbers])
            print(output_numbers)


if __name__ == "__main__":
    main()