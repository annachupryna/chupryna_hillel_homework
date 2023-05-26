"""
    Task 2
    Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
    the perimeter of the square, the area of the square, and the diagonal of the square.
"""
import math


def square(side: int) -> tuple:
    perimeter = side * 4
    area = pow(side, 2)
    diagonal = round(math.sqrt(2) * side, 2)
    return perimeter, area, diagonal
