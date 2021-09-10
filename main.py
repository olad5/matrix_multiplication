#!/usr/bin/python3
# This is a python file to calculate the geometric mean of an arbitary number
# of positive numbers
import sys
import logging
logging.basicConfig(
    level=logging.DEBUG, format="Line %(lineno)d - %(message)s",)

class Matrix_Multi:
    def __init__(self):
        self.numbers = []
        INPUT_FILES = ('matrix1.txt', 'matrix2.txt')
        self.matrix_1 = self.read_input_file(INPUT_FILES[0])
        self.matrix_2 = self.read_input_file(INPUT_FILES[1])

    def read_input_file(self, file):
        with open(file) as input1:
            # gets the contents of files
            content =  input1.readlines()
            # separates them by ','
            row1  = (content[0]).split(',')
            row2  = (content[1]).split(',')
            num_rows  = len(row1)
            num_columns  = len(content)

            # strips new line characters
            matrix_values  = [x.strip() for x in row1+row2]
            # save the matrix properties into a dictionary
            props = {
                "rows": num_rows,
                "columns": num_columns,
                "values": matrix_values,
            }

            return props



if __name__ == '__main__':
    m = Matrix_Multi()
