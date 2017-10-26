#!usr/bin/env python3
"""
Calculate Distance

Solution Author: Mild Z Ferdinand

Description: You have coordinates of 2 points and need to find the distance
between them.
"""
import re
import sys


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            coords = line.strip()
            x1, y1, x2, y2 = list(map(int, re.findall('-*\d+', coords)))
            x = (x1 - x2) ** 2
            y = (y1 - y2) ** 2
            distance = (x + y) ** 0.5
            print(int(distance))


if __name__ == "__main__":
    main()