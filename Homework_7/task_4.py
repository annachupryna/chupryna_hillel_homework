"""
    Task 4
    Implement your own implementation of function max and min (* additional argument amount of result, if you pass 2,
    function should return 2 max values from the list)
"""


def custom_sorting_max(list_of_values, amount):
    for i in range(len(list_of_values)):
        for j in range(len(list_of_values) - 1):
            if list_of_values[j] < list_of_values[j + 1]:
                list_of_values[j], list_of_values[j + 1] = list_of_values[j + 1], list_of_values[j]

    return list_of_values[:amount]


def custom_sorting_min(list_of_values, amount):
    for i in range(len(list_of_values)):
        for j in range(len(list_of_values) - 1):
            if list_of_values[j] > list_of_values[j + 1]:
                list_of_values[j], list_of_values[j + 1] = list_of_values[j + 1], list_of_values[j]

    return list_of_values[:amount]
