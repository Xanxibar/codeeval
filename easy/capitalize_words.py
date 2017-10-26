#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Capitalize Words

Challenge Description:

Write a program which capitalizes the first letter of each word in a sentence.
"""
import sys

input_file = sys.argv[1]


def main():
    with open(input_file, 'r') as text:
        for line in text:
            mystring = line.strip()
            new_string = []
            for word in mystring.split():
                new_word = word[0].upper() + word[1:]
                new_string.append(new_word)
            print(" ".join(new_string))
    return True


if __name__ == "__main__":
    main()