"""
    Task 2
    Implement your realization of the function filter
"""


def custom_filter(func, array):
    filtered_array = []
    for element in array:
        if func(element):
            filtered_array.append(element)
    return filtered_array
