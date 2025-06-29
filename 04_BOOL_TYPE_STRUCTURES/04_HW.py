#Task 01
print('\n---Task 01---')
str_var = input('Pls, enter your string: ')
print((str_var[:2] + str_var[-2:]) if len(str_var) >= 2 else '')


#Task 02
print('\n---Task 02---')
tel_num = input('Pls, enter your phone number: ')
# print('Number is OK' if len(tel_num) == 10 and tel_num.isdigit() else 'You\'ve entered something wrong')
if tel_num.isdigit():
    str_len = len(tel_num)
    if str_len == 10:
        print('Telephone number is OK')
    else:
        print(f'You have entered {str_len} digits instead of 10... ')
else:
    print('You have entered not digits...')


#Task 03
print('\n---Task 03---')

a = int(input('Pls, enter first digit: '))
b = int(input('Pls, enter second digit: '))

# ADDITION
add_res = int(input(f'What is the result for {a} + {b} ? '))
result = a + b
print('--> CORRECT' if add_res == result else f'--> NOT CORRECT... ANSWER is {result} ')

# SUBTRACTION
substr_res = int(input(f'What is the result for  {a} - {b} ? '))
result = a - b
print('--> CORRECT' if substr_res == result else f'--> NOT CORRECT... ANSWER is {result} ')

# DIVISION
div_res = float(input(f'What is the result for  {a} / {b} with 1 sign after coma? '))
result = round(a / b, 1)
print('--> CORRECT' if div_res == result else f'--> NOT CORRECT... ANSWER is {result:.1f} ')

# MULTIPLICATION
mult_res = int(input(f'What is the result for  {a} * {b} ? '))
result = a * b
print('--> CORRECT' if mult_res == result else f'--> NOT CORRECT... ANSWER is {result} ')

#EXPONENT (POWER)
pow_res = int(input(f'What is the result for  {a} ** {b} ? '))
result = a ** b
print('--> CORRECT' if pow_res == result else f'--> NOT CORRECT... ANSWER is {result} ')

# MODULUS
mod_res = int(input(f'What is the result for  {a} % {b} ? '))
result = a % b
print('--> CORRECT' if mod_res == result else f'--> NOT CORRECT... ANSWER is {result} ')

#FLOOR DIVISION
floor_res = int(input(f'What is the result for  {a} // {b} ? '))
result = a // b
print('--> CORRECT' if floor_res == result else f'--> NOT CORRECT... ANSWER is {result} ')

#Task 04
print('\n----Task 04----')

MY_NAME = 'batyrbek'
var_name = input('Pls, enter your name: ')
print('--- CORRECT' if MY_NAME == var_name.lower() else '--- NOT CORRECT')


