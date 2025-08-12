# 1 ====================================================================================================================
"""Task 1

Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters:
 'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function"""
from Demos.GetSaveFileName import customfilter


class with_index:
    def __init__(self, iterable, start = 0):
        self.show_index = start
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        # try:
        #     self.show_index += 1
        #     return self.show_index - 1, next(self.iterator)
        # except StopIteration:
        #     raise
        self.show_index += 1
        return self.show_index - 1, next(self.iterator)

# TESTING
# test_set = {1, 2, 3, 4, 5}
# test_dict = my_dict = {
#     "apple": 3,
#     "banana": 5,
#     "cherry": 7,
#     "date": 2,
#     "elderberry": 4,
#     "fig": 9,
#     "grape": 6
# }
# test_str = 'abcdefghijklmnopqrstuvwxyz'
# for index, value in with_index(test_str, 1):
#     print(f'{index}: {value}')

# 2 ====================================================================================================================
"""Task 2

Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
 'start', 'end', and optional step. Tips: See the documentation for 'range' function"""
def my_range(*args):
    if any(not isinstance(argument, int) for argument in args):
        raise TypeError('Arguments must be int type')
    if len(args) == 0:
        raise TypeError('You did not provide enough arguments')
    elif len(args) == 1:
        stop = args[0]
        start = 0
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
    if step == 0:
        raise ValueError('Step cannot be 0')
    current_index = start
    if step > 0 :
        while current_index < stop:
            yield current_index
            current_index += step
    elif step < 0:
        while current_index > stop:
            yield current_index
            current_index += step

# TESTING
# print(list(my_range(5)))          # [0, 1, 2, 3, 4]
# print(list(my_range(2, 7)))       # [2, 3, 4, 5, 6]
# print(list(my_range(10, 2, -2)))  # [10, 8, 6, 4]
# print(list(my_range(0, 10, 3)))   # [0, 3, 6, 9]

# 3 ====================================================================================================================
"""Task 3

Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax."""
class MyIterable:
    def __init__(self, data = []):
        self.data = list(data)

    def custom_iterator(self):
        for i in range(len(self.data)):
            yield self.data[i]

    def __iter__(self):
        return self.custom_iterator()

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

