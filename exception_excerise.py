import sys
import math


class Circle:
    def __init__(self, radius):
        try:
            if not radius.isnumeric():
                raise ValueError('RadiusInputError')
        except ValueError as e:
                print("'hello' is not a number")  

      

c1 = Circle('hello')

try:
    f = open('unknown_file.txt')
    print(f.read())

except FileNotFoundError as e:
    print('File not found.')

try:
    data = input("")
    if len(data) > 10:
        raise ValueError('Input String contains more than 10 characters.')
except  ValueError as e:
    print(e)



try:
    data = int(input(""))
    if not (data >= 0 and data <= 100):
        raise ValueError('Input integer value must be between 0 and 100.')
except  ValueError as e:
    print(e)
