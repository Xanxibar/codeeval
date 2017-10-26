#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Lowest unique number

Challenge Description:

There is a game where each player picks a number from 1 to 9, writes it on a
paper and gives to a guide. A player wins if his number is the lowest unique.
We may have 10-20 players in our game.
Print a winner's position or 0 in case there is no winner.
"""
from collections import Counter
import sys

input_file = sys.argv[1]


def main():
    with open(input_file, 'r') as text:
        for line in text:
            rounds = line.strip().split()
            nums = Counter(rounds)
            uniques = []
            for i, v in nums.items():
                if v == 1:
                    uniques.append(int(i))
            if uniques:
                minimum = str(min(uniques))
                print(rounds.index(minimum) + 1)
            else:
                print(0)

    return True


if __name__ == "__main__":
    main()