#!usr/bin/env python3
"""
Find A Writer

Solution Author: Mild Z Ferdinand

Description:  You have a set of rows with names of famous writers encoded
inside. Each row is divided into 2 parts by pipe char (|). The first part has a
writer's name. The second part is a "key" to generate a name.
Your goal is to go through each number in the key (numbers are separated by
space) left-to-right. Each number represents a position in the 1st part of a
row. This way you collect a writer's name which you have to output.
"""
import sys


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            cipher, key = line.strip().split('|')
            key = list(map(int, key.strip().split()))
            name = []
            for i in key:
                name.append(cipher[i - 1])
            print("".join(name))

if __name__ == "__main__":
    main()