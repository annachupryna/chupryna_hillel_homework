"""
    Task 4
    You have a file of unknown length. Write a function that will remove all numbers from each line of the file.
"""
import re


def remove_numbers(text_file):
    with open(text_file, 'r+') as file:
        data = file.read()
        updated_file = re.sub(r'[0-9]+', '', data)
    with open(text_file, 'w') as file:
        file.write(updated_file)
