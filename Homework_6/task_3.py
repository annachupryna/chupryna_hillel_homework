"""
    Task 3
    Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is
    a prime number, and False otherwise.
"""


def is_prime(number):
    if number > 1000 or number <= 1:
        return f'Please, enter a number from 2 to 1000'
    else:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True
