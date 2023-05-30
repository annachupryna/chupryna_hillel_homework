"""
    Task 7
    Write a function with the following signature: def display_box(width: int, height: int, character="*") .
    This function will draw a simple ASCII-art rectangle (non-filled) of the given height and width, using character to
    print the lines. For example, display_box(5, 4, 'x') should output the following:
    xxxxx
    x _ x
    x _ x
    xxxxx
"""


def display_box(width: int, height: int, character):
    for row in range(height):
        if row == 0 or row == height - 1:
            print(character * width)
        else:
            empty = width - 2
            print(character + (" " * empty) + character)
