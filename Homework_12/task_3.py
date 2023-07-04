"""
3. Create an iterator that accepts a sequence and can iterate over values over a given range.
CustomIterator(sequence, start_index, end_index)
"""


class CustomIterator:
    def __init__(self, sequence: list, start_index, end_index):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index
        self.__current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < self.__end_index:
            value = self.__sequence[self.__current_index]
            self.__current_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5]
    my_iterator = CustomIterator(seq, 1, 5)
    for item in my_iterator:
        print(item)
