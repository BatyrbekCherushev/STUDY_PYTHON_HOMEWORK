import json

def add_new_entries():
    first_name = input('Enter your first name: ').capitalize()
    last_name = input('Enter your last name: ').capitalize()
    telephone_number = input('Enter your telephone number: ')
    city = input('Enter your city: ')
    state = input('Enter your state: ')
    my_dict[telephone_number] = {'first_name': first_name,
                                 'last_name': last_name,
                                 'full_name' : first_name + ' ' + last_name,
                                 'city': city,
                                 'state': state}

def save_book():
    with open('test.json', 'w', encoding='utf-8') as f_o:
        json.dump(my_dict, f_o, indent=4, ensure_ascii=False)

def show_book():
    print('______________________________________')
    for key in my_dict:
        print(key, ':', my_dict[key])
    print('______________________________________')

def search_entry(key, value):
    if key == 'phone' and value in my_dict:
        return value, my_dict[value]
    else:
        result = []
        for k in my_dict:
            if value.lower() == my_dict[k][key].lower() :
                result.append((k, my_dict[k]))
        if len(result) > 0:
            return result
    return None


with open('test.json', 'r', encoding='utf-8') as file_object:
    my_dict = json.load(file_object)

while True:
    my_choice = input('Do your choice, pls:\n'
                      '0 - program exit;\n'
                      '1 - Add new entries;\n'
                      '2 - SHOW phonebook;\n'
                      '3 - SEARCH by name;\n'
                      '4 - SEARCH by last name;\n'
                      '5 - SEARCH by fullname;\n'
                      '6 - SEARCH by phone;\n'
                      '7 - SEARCH by city;\n'
                      '8 - SEARCH by state;\n '
                      )
    if my_choice == '0':
        break
    elif my_choice == '1':
        add_new_entries()
        save_book()
    elif my_choice == '3':
        print(search_entry('first_name', input('Pls enter the name for SEARCH: ')))
    elif my_choice == '4':
        print(search_entry('last_name', input('Pls enter the last name for SEARCH: ')))
    elif my_choice == '5':
        print(search_entry('full_name', input('Pls enter the full name for SEARCH: ')))
    elif my_choice == '6':
        print(search_entry('phone', input('Pls enter the phone for SEARCH: ')))
    elif my_choice == '7':
        print(search_entry('city', input('Pls enter the city for SEARCH: ')))
    elif my_choice == '8':
        search_result = search_entry('state', input('Pls enter the state for SEARCH: '))
        for i in search_result:
            print(search_result[i])
    elif my_choice == '2':
        show_book()


