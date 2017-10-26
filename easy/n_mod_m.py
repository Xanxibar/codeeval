#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Description: Given two integers N and M, calculate N Mod M
(without using any inbuilt modulus operator).
"""
import sys


def my_mod(n, m):
    """Returns the remainder of division operation on two numbers."""
    while n >= m:
        n -= m
    return n


def file_lines():
    """Returns the values of each line of the input file as a tuple."""
    try:
        input_file = sys.argv[1]
    except:
        return "Please provide file name as command line argument."
    with open(input_file, 'r') as text:
        for line in text:
            n, m = tuple(map(int, line.strip().split(',')))
            yield (n, m)


def main():
    for i, v in file_lines():
        print(my_mod(i, v))


if __name__ == "__main__":
    main()
