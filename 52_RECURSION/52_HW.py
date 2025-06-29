#-------------------------> TASK-01 <---------------------------
def to_power(x, exp):
    if exp < 0:
        return 'This function works only with exp > 0'
    if exp == 0:
        return 1

    if exp == 1:
        return x

    return to_power(x, exp - 1) * x

#-------------------------> TASK-02 <---------------------------
def is_palindrome(looking_str):
    if len(looking_str) == 1 or len(looking_str) == 0:
        return True
    return is_palindrome(looking_str[1:-1]) and (looking_str[0] == looking_str[-1])


#-------------------------> TASK-03 <---------------------------
def mult(a, n):
    if n == 0:
        return 0
    if n == 1:
        return a
    return mult(a, n - 1) + a


#-------------------------------> Task_04 <-----------------------------------
def reverse_str(input_str):
    if len(input_str) == 1:
        return input_str
    return reverse_str(input_str[1:]) + input_str[0]

#-------------------------> TASK-05 <---------------------------
def sum_of_digits(digit_string):
    if len(digit_string) == 1:
        return int(digit_string)
    return sum_of_digits(digit_string[1:]) + int(digit_string[0])