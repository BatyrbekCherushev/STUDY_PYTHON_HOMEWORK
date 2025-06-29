#-------------------------> TASK-01 <----------------------------
print('TASK-01 --------->')

sentence_list = input('Pls enter some sentence: ').strip().split(' ')

print({word: sentence_list.count(word) for word in set(sentence_list)})

# -------------------------> TASK-02 <----------------------------
print('\nTASK-02 --------->')

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock_sums = {key: stock[key] * prices[key] for key in stock}
for key in stock_sums:
    print(f'{key}: {stock_sums[key]}')


# -------------------------> TASK-03 <----------------------------
print('\nTASK-03 -----------> ')

print([(i, i ** 2) for i in range(1, 11)])

# -------------------------> TASK-04 <----------------------------
print('\nTASK-04 -----------> ')

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

first_dict = {i + 1: days[i] for i in range(len(days))}
print(first_dict)
print({value: key for key, value in first_dict.items()})