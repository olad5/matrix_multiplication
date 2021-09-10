#!/usr/bin/python3
# This is a python file to calculate the  multiplication of two matrices

class Matrix_Multi:
    def __init__(self):
        self.matrix_1 = self.read_input_file('matrix1.txt')
        self.matrix_2 = self.read_input_file('matrix2.txt')
        self.cal_multi(self.matrix_1, self.matrix_2)

    def read_input_file(self, file):
        with open(file) as file:
            # gets the contents of files
            content =  file.readlines()
            matrix  = [ [int(num.strip()) for num in content[x].split(',')]  for x in  range(len(content))]
            return matrix

    def cal_multi(self, matrix_1, matrix_2):
        if len(matrix_1[0]) != len(matrix_2):
            print(" You can't multi these two matrices\n")
            return
        result = [[0 for x in range(len(matrix_2))] for y in
                  range(len(matrix_1))]
        # loop through rows of X
        for i in range(len(matrix_1)):
            # loop through columns of Y
            for j in range(len(matrix_2[0])):
                # loop through rows of Y
                for k in range(len(matrix_2)):
                   result[i][j] += matrix_1[i][k] * matrix_2[k][j]

        for row in result:
            print(row)

if __name__ == '__main__':
    m = Matrix_Multi()
