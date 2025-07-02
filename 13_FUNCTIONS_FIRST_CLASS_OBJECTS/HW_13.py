# =============================================> TASK-01 (chatGPT help was used) <==================================
"""Write a Python program to detect the number of local variables declared in a function."""
def get_locals_num_no_args(func):
    code = func.__code__
    print(f'Function {func.__name__} has {code.co_nlocals - code.co_argcount - code.co_kwonlyargcount} without arguments')

def get_locals_num_all(func):
    print(f'Function {func.__name__} has {func.__code__.co_nlocals} including arguments')

def do_something(a, b, c):
    int_var = 1
    float_var = .5
    str_var = 'Hello'
    bool_var = False

get_locals_num_all(do_something)
get_locals_num_no_args(do_something)


# =============================================> TASK-02 <==================================
"""Write a Python program to access a function inside a function (Tips: use function, which returns another function)"""
def decorate_func():
    def wrap_func():
        print('I am wrapper of some future function')

    return wrap_func

decorate_func()()


# ====================> TASK-03 <==================================
"""Write a function called "choose_func" which takes a list of nums and 2 callback functions.
 If all nums inside the list are positive, execute the first function on that list and return the result of it.
  Otherwise, return the result of the second one"""
def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

def choose_func(some_list, func_pos, func_neg):
    are_positive = all(i > 0 for i in some_list)
    if are_positive:
        return func_pos(some_list)
    else:
        return func_neg(some_list)

print(choose_func([1,2, 1,0], square_nums, remove_negatives))
print(choose_func([-1,2, 1,3], square_nums, remove_negatives))
print(choose_func([1,2, 3,4], square_nums, remove_negatives))

