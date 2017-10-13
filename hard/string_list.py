#!usr/bin/env python3

"""
string_list.py
author: Mild Z Ferdinand

description: You are given a number N and a string S. Print all of the
possible ways to write a string of length N from the characters in string S,
comma delimited in alphabetical order.
"""
import sys
from itertools import product

input_file = sys.argv[1]


def main():
    with open(input_file, 'r') as text:
        for line in text:
            num, mystring = line.strip().split(',')
            permutations = product(mystring, repeat=int(num))
            unique_permutations = set(permutations)  # filter out duplicates
            joined_permutations = [''.join(i) for i in unique_permutations]
            print(','.join(sorted(joined_permutations)))
    return True


if __name__ == "__main__":
    main()