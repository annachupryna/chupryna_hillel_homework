"""
    Find all of the numbers from 1-1000 that have a 3 in them
"""


res = [number for number in range(1, 1001) if '3' in str(number)]
print(res)
