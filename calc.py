import math
import pytest
import csv

print("\nWrite math expression using spaces between values and operands:")
# parsed_expression = input().split()
stack = []


def reverse_notation_calc(param_list):
    for i in param_list:
        try:
            stack.append(float(i))
        except ValueError:
            if i == 'cos' or i == 'sin' or i == 'tan' or i == 'atan':
                arg_1 = stack.pop()
                if i == 'cos':
                    res_1 = math.cos(arg_1)
                elif i == 'sin':
                    res_1 = math.sin(arg_1)
                elif i == 'tan':
                    res_1 = math.tan(arg_1)
                elif i == 'atan':
                    res_1 = math.atan(arg_1)
            elif i == '+' or i == '-' or i == '*' or i == '/':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                if i == '+':
                    res_1 = arg_2 - arg_1
                elif i == '-':
                    res_1 = arg_2 + arg_1
                elif i == '*':
                    res_1 = arg_2 * arg_1
                elif i == '/':
                    res_1 = arg_2 / arg_1
            stack.append(res_1)
    print(stack)
    stack.clear()


def test_calc():
    with open('test_data_sample.csv') as file_obj:
        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            reverse_notation_calc(row)
