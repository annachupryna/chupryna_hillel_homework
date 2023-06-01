"""
    Task 1
    Implement your own print function. It should work on all operating systems. You can't use build-in print function
"""


def custom_print(user_input: str):
    import sys
    sys.stdout.write(user_input)
