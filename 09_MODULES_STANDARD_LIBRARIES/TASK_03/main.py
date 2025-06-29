import os
import mymod

file_name = input('Pls, enter filename you want to handle: ')
if os.path.exists(file_name):
    print(f"'{file_name}' has: \n\t{mymod.count_lines(file_name)} lines\n\t{mymod.count_chars(file_name)} characters")
else:
    print('---> File does not exist')