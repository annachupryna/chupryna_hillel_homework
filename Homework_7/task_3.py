"""
    Task 3
    Implement your own implementation of the function map
"""


def custom_map(func, array):
    filtered_array = []
    for element in array:
        filtered_array.append(func(element))
    return filtered_array


sample = [1, 2, 3, 4, 5]
print(custom_map(lambda x: x * 2, sample))
