#!usr/bin/env python3
"""Self Describing Numbers

Challenge Description:

A number is a self-describing number when (assuming digit positions are labeled
0 to N-1), the digit in each position is equal to the number of times that
that digit appears in the number.

If the number is a self-describing number, print out 1. If not, print out 0.

solution by: Mild Z Ferdinand
"""
from collections import Counter
import sys

input_file = sys.argv[1]
ctr = Counter()


def describe(cntr, nums):
    for i in range(len(nums)):
        digit = nums[i]
        if int(digit) != int(cntr[str(i)]):
            print(0)
            return False
    print(1)
    return True


def main():
    with open(input_file, 'r') as text:
        for line in text:
            nums = list(line.strip())      # create a list of digits
            ctr.update(nums)               # Update counter with tally of digits
            describe(ctr, nums)
            ctr.clear()
    return True


if __name__ == "__main__":
    main()
