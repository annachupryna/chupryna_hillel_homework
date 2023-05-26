"""
    Task 6
    Write a function that takes in a string and returns the string with all the vowels removed.
"""
import re


def remove_vowels(string: str):
    updated_string = re.sub(r'[aueioy]+', '', string)
    return updated_string
