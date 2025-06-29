import random

#TASK-01
print('----TASK-01----')

new_list = []
i = 0
while i <= 9:
    new_list.append(random.random())
    i += 1
print(new_list)
print(f'MAX number of the list is {max(new_list)}')

#TASK-02
print('\n----TASK-02----')

list_01 = []
list_02 = []

i = 0
while i <= 9:
    list_01.append(random.randint(1, 10))
    list_02.append(random.randint(1, 10))
    i += 1
print('List #1: ', list_01)
print('List #2: ',list_02)
print('List without repeats: ', list(set(list_01) & set(list_02)))

#TASK-03
print('\n----TASK-03----')

list_100 = list(range(1, 101))
print('Initial list: ', list_100)

new_list = []
i = 0
while i <= (len(list_100) - 1):
    if list_100[i] % 7 == 0 and list_100[i] % 5 != 0:
        new_list.append(list_100[i])
    i += 1

print('Result list: ', new_list)