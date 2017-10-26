#!usr/bin/env python3

"""
Penultimate Word
Solution Author: Mild Z Ferdinand
Description: Write a program that finds the next to last word in a string.
"""
import sys


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            whole_string = line.strip()
            penultimate_word = whole_string.split()[-2]
            print(penultimate_word)


if __name__ == "__main__":
    main()