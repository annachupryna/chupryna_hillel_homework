"""
    Task 5
    Implement your own all function
"""


def custom_all(custom_list):
    for el in custom_list:
        if not el:
            return False
    return True
