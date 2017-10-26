#!usr/bin/env python3
"""
Author: Mild Z Ferdinand
Description: Finds the maximum beauty of a string.
"""
from collections import Counter
import sys


def max_beauty(astring):
    """Returns a value representing the beauty of a string."""
    my_string = filter(str.isalpha, astring.lower())
    cntr = Counter(my_string)
    value = 26
    total = 0
    for i, v in sorted(cntr.items(), key=lambda x: x[1])[::-1]:
        total += int(v) * value
        value -= 1
    return total


def main():
    try:
        input_file = sys.argv[1]
    except:
        return "Please enter path to file as a command line argument."
    with open(input_file, 'r') as text:
        for line in text:
            my_string = line.strip()
            print(max_beauty(my_string))
    return True


if __name__ == "__main__":
    main()