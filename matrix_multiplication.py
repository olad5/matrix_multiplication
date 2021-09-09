#!/usr/bin/python3
# This is a python file to calculate the geometric mean of an arbitary number
# of positive numbers


class Matrix_Multi:
    def __init__(self):
        self.numbers = []
        # print('hello')
        self.read_input_file()
        # self.cal_arit_mean()
        # print()
        # self.cal_geo_mean()

    def read_input_file(self):
        with open('matrices1.txt') as input1:
            matrix_1 =  input1.readlines()
            for  line in matrix_1:
                print(type( line ))

    def cal_arit_mean(self):
        total = 0
        for num in self.numbers:
            total += num
        self.avg = total / len(self.numbers)
        print(f"The arithmetic mean is {self.avg}")

    def cal_geo_mean(self):
        product_numbers = 1
        for num in self.numbers:
            product_numbers *= num
        self.geo_mean = product_numbers**(1/len(self.numbers))
        print(f"The geometric mean is {self.geo_mean}")


if __name__ == '__main__':
    m = Matrix_Multi()
