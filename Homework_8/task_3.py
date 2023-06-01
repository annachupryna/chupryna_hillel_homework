"""
    Find all of the numbers from 1-1000 that are divisible by 7
"""


res = [number for number in range(1, 1001) if number % 7 == 0]
print(res)
