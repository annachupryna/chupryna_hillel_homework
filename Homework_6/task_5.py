"""
    Task 5
    Create a function that accepts N parameters of type int. Calculate the sum of these parameters and return it.
"""


def calculate_params(*args: int):
    return sum(args)
