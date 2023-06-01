"""
    Create a decorator that prints to the console the name of the function that was called. The function should work
    as intended. For example, create a pair of functions for the arithmetic operations of summation and multiplication.
    When calling these functions, the result of the operation must be returned and the name of the function that was
    called must be displayed in the console with the result. Small hint (__name__)
"""


def print_function_name(func):
    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        result = func(*args)
        return result
    return wrapper


@print_function_name
def summation(*args):
    res = 0
    for el in args:
        res += el
    return res


@print_function_name
def multiplication(*args):
    res = 1
    for el in args:
        res *= el
    return res


if __name__ == '__main__':
    print(summation(1, 2, 4, 5))
    print(multiplication(2, 2, 8, 9))
