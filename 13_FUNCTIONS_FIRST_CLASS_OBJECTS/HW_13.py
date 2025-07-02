# =============================================> TASK-01, TASK-02 <==================================
def do_some():
    int_var = 10
    float_var = .5
    str_var = 'dsakl;dsa'
    vars_num = len(locals())

    def get_vars():
        return vars_num

    return get_vars

get_func_vars = do_some()

print(get_func_vars())


# ====================> TASK-03 <==================================
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

