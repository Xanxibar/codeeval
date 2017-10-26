#!usr/bin/env python3
"""
Longest Word
Solution Author: Mild Z Ferdinand
Description: In this challenge you need to find the longest word in a sentence.
If the sentence has more than one word of the same length you should pick the
first one.
"""
import sys


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            case = line.strip().split()
            longest = 0
            length = 0
            myword = None
            for word in case:
                length = len(word)
                if length > longest:
                    longest = length
                    myword = word
            print(myword)
    return True


if __name__ == "__main__":
    main()