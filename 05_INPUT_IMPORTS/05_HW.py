import random

#---TASK-01---
print('\n---TASK_01---')

is_running = True
while is_running:
    user_choice = input('Pls input number from 1 to 10 (or "exit" to quit): ').strip().lower()
    if user_choice == 'exit':
        break
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 1 <= user_choice <= 10:
            if user_choice == random.randint(1, 10):
                print('Good job, bro!')
                is_running = False
            else:
                print('Not this time, mate. Let us try agan...')
        else:
            print('---> RANGE ERROR: You have entered a digit out of range [1:10], pls try again...')
    else:
        print('---> INPUT ERROR: You have entered not a digit, pls try again')

#---TASK-02---
print('\n---TASK_02---')

user_name = input('Pls, enter your name: ').strip().capitalize()

while True:
    user_age = input('Pls, enter your age: ').strip()
    if user_age.isdigit():
        print(f"Hello {user_name}, on your next birthday you’ll be {int(user_age) + 1} years")
        break
    else:
        print('---> INPUT ERROR: You have entered not a digit as age, pls try again')

#---TASK-03---
print('\n---TASK_03---')

user_str = input('Pls, enter your string: ').strip()

for i in range(5):
    temp_str = user_str[:]
    result = ''

    while len(temp_str) > 0:
        char = random.choice(temp_str)
        result = result + char
        temp_str = temp_str.replace(char,'', 1)
    print(result)








