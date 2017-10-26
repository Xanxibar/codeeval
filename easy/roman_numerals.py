#!usr/bin/env python3
"""
Roman Numerals
Solution Author: Mild Z Ferdinand
Description: Write a program to convert a cardinal number to a Roman numeral.
"""
from collections import deque
import sys


NUMERALS = {
    '1': 'I',
    '2': 'II',
    '3': 'III',
    '4': 'IV',
    '5': 'V',
    '6': 'VI',
    '7': 'VII',
    '8': 'VIII',
    '9': 'IX',
    '10': 'X',
    '20': 'XX',
    '30': 'XXX',
    '40': 'XL',
    '50': 'L',
    '60': 'LX',
    '70': 'LXX',
    '80': 'LXXX',
    '90': 'XC',
    '100': 'C',
    '200': 'CC',
    '300': 'CCC',
    '400': 'CD',
    '500': 'D',
    '600': 'DC',
    '700': 'DCC',
    '800': 'DCCC',
    '900': 'CM',
    '1000': 'M',
    '2000': 'MM',
    '3000': 'MMM',
    }


def cardinal_to_roman(number_string):
    """Converts a cardinal number to a roman numeral."""
    num_list = deque(number_string)
    rom_nums = deque()
    pos = 0.1
    while True:
        pos = int(pos * 10)
        try:
            num = str(int(num_list.pop()) * pos)
            if num == '0':
                continue
        except:
            break
        value = NUMERALS[num]
        rom_nums.appendleft(value)
    return "".join(rom_nums)


def main():
    with open(sys.argv[1], 'r') as text:
        for line in text:
            rom_nums = line.strip()
            print(cardinal_to_roman(rom_nums))
    return True


if __name__ == "__main__":
    main()
