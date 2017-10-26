#!usr/bin/env/ python3

"""
Author: Mild Z Ferdinand
Description: Hex to Decimal challenge. You will be given a hexadecimal(base 16)
number. Convert it into decimal (base 10).
"""
import sys


def main():
    try:
        input_file = sys.argv[1]
    except:
        return "Please supply file name as a command line argument"
    with open(input_file, 'r') as text:
        for line in text:
            num = line.strip()
            print(int(num, 16))
    return True

if __name__ == "__main__":
    main()