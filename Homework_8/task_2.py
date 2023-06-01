"""
    Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
    The solution should work and not freeze your computer.
"""


def my_gen():
    for i in range(1000000001):
        if i % 2 == 0:
            yield pow(i, 2)


if __name__ == '__main__':
    my_custom_gen = my_gen()
    for el in my_gen():
        print(el)
