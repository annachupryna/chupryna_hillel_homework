# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_index = []
even_index_numbers = []
odd_index = []
odd_index_numbers = []
for index, number in enumerate(numbers):
    odd_or_even_index = index % 2
    if odd_or_even_index == 0:
        even_index.append(index)
        even_index_numbers.append(number)
    else:
        odd_index.append(index)
        odd_index_numbers.append(number)

list_of_even_indexes = list(zip(even_index, even_index_numbers))
list_of_odd_indexes = list(zip(odd_index, odd_index_numbers))
print(f'This is a list of even indexes and its numbers: {list_of_even_indexes}')
print(f'This is a list of odd indexes and its numbers: {list_of_odd_indexes}')
