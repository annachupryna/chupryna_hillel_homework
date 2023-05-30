"""
    Task 5
    Implement your own all function
"""


def custom_all(custom_list):
    define_list = []
    for el in range(len(custom_list)):
        if custom_list[el]:
            define_list.append(True)
        else:
            define_list.append(False)
    if False in define_list:
        return False
    else:
        return True
