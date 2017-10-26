#!usr/bin/env python3

"""
Author: Mild Z Ferdinand
Query Board

Challenge Description:

There is a board (matrix). Every cell of the board contains one integer, which
is 0 initially.

The next operations can be applied to the Query Board:

SetRow i x: it means that all values in the cells on row "i" have been changed
to value "x" after this operation.

SetCol j x: it means that all values in the cells on column "j" have been
changed to value "x" after this operation.

QueryRow i: it means that you should output the sum of values on row "i".

QueryCol j: it means that you should output the sum of values on column "j".

The board's dimensions are 256x256
"i" and "j" are integers from 0 to 255
"x" is an integer from 0 to 31
"""
import sys

input_file = sys.argv[1]


class Matrix(object):

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.matrix = []
        for i in range(self.rows):
            a_row = []
            for e in range(self.cols):
                a_row.append(0)
            self.matrix.append(a_row)

    def setRow(self, row, value):
        """Sets the value of an entire row."""
        for i in range(self.cols):
            self.matrix[row][i] = value

    def setCol(self, col, value):
        """Sets the value of an entire column."""
        for i in range(self.rows):
            self.matrix[i][col] = value

    def queryRow(self, row):
        """Returns the sum of the values in the row."""
        return sum(self.matrix[row])

    def queryCol(self, col):
        """Returns the sum of the values in a column."""
        return sum([row[col] for row in self.matrix])


def main():
    matrix = Matrix(256, 256)
    with open(input_file, 'r') as text:
        for line in text:
            command = line.strip().split()
            if command[0] == "SetRow":
                matrix.setRow(int(command[1]), int(command[2]))
            elif command[0] == "SetCol":
                matrix.setCol(int(command[1]), int(command[2]))
            elif command[0] == "QueryRow":
                print(matrix.queryRow(int(command[1])))
            elif command[0] == "QueryCol":
                print(matrix.queryCol(int(command[1])))
    return True


if __name__ == "__main__":
    main()