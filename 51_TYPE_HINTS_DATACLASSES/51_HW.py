import sys, os, json
import colorama

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VALUES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
MAX_BOOK_SIZE: int = 100
DEFAULT_FILE_NAME:str = 'default_book.json'
GOOD_KEYS:list[str] = ['name', 'lastname', 'tel', 'city', 'state']
MAIN_MENU:list[str] = [
    '0: QUIT',
    '1: OPEN phonebook',
    '2: CREATE new phone book'
]
BOOK_MENU:list[str] = ['3: SHOW phonebook',
             '4: ADD new entry in phonebook',
             '5: SEARCH by name',
             '6: SEARCH by lastname',
             '7: SEARCH by full name',
             '8: SEARCH by city',
             '9: SEARCH by state',
             '10: SEARCH by name, lastname, tel, city, state',
             '11: DELETE all entries in the phonebook'
]
EDIT_MENU:list[str] = ['0 - QUIT SEARCH',
             '1 - UPDATE ENTRY',
             '2 - DELETE ENTRY']

#colors
RESET_COLORS = colorama.Style.RESET_ALL
TEXT_RED = colorama.Fore.RED
TEXT_GREEN = colorama.Fore.GREEN
TEXT_YELLOW = colorama.Fore.YELLOW
TEXT_CYAN = colorama.Fore.CYAN
TEXT_ROSA = colorama.Fore.MAGENTA

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> DEFINE FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def show_menu(menu_list:list[str]):
    for i in range(len(menu_list)):
        print(TEXT_YELLOW + '['+ RESET_COLORS + menu_list[i] + TEXT_YELLOW + '] ', end = '', )
        if i % 6 == 0 and i != 0:
            print()
    print()
    print(TEXT_YELLOW + '--->' + RESET_COLORS)

def show_edit_menu(book:dict):
    while True:
        show_menu(EDIT_MENU)
        edit_choice = input('Pls choose operation: ')
        match edit_choice:
            # QUIT SEARCH
            case '0':
                break

            # UPDATE entry
            case '1':
                update_id = input('Pls enter ID of entry you want to UPDATE: ')
                if update_id in book:
                    book[update_id] = create_entry()
                else:
                    print(TEXT_RED + f'NO SUCH ID {update_id}' + RESET_COLORS)
            # DELETE entry
            case '2':
                delete_id = input('Pls enter ID of entry you want to DELETE: ')
                if delete_id in book:
                    del book[delete_id]
                else:
                    print(TEXT_RED + f'NO SUCH ID {delete_id}' + RESET_COLORS)


def open_book(name:str, used_book:dict):
    try:
        with open(name, encoding = 'utf-8') as fo:
            return json.load(fo)
    except FileNotFoundError as err_inst:
        print(TEXT_RED + '---> NO SUCH FILE...')
        return used_book

def save_book(filename:str, book:dict):
    with open(filename, 'w', encoding = 'utf-8') as f_o:
        json.dump(book, f_o, indent = 4, ensure_ascii = False)

def create_entry(info_list:dict = None, **kwargs):
    """ Function to create and return new entry fo phone book
    - you can to put ur dictionary with user info as first argument
    - if there is no info_list argument or it does not contain specific key -> checking **kwargs for specific key
    - if **kwargs doesn`t have a specific key -> going to user input for value for specific key """
    entry = {}

    # ADDING name
    if type(info_list) is dict and 'name' in info_list:
        entry['name'] = info_list['name'].capitalize()
    elif 'name' in kwargs:
        entry['name'] = kwargs['name'].capitalize()
    else:
        entry['name'] = input('Pls enter the user name: ').capitalize()

    # ADDING last name
    if type(info_list) is dict and 'last_name' in info_list:
        entry['last_name'] = info_list['last_name'].capitalize()
    elif 'last_name' in kwargs:
        entry['last_name'] = kwargs['last_name'].capitalize()
    else:
        entry['last_name'] = input('Pls enter the user surname: ').capitalize()

    # ADDING phone
    if type(info_list) is dict and 'tel' in info_list:
        entry['tel'] = info_list['tel']
    elif 'tel' in kwargs:
        entry['tel'] = kwargs['tel']
    else:
        entry['tel'] = input('Pls enter the user phone number: ')

    # ADDING city
    if type(info_list) is dict and 'city' in info_list:
        entry['city'] = info_list['city']
    elif 'city' in kwargs:
        entry['city'] = kwargs['city']
    else:
        entry['city'] = input('Pls enter the user city: ')

    # ADDING state
    if type(info_list) is dict and 'state' in info_list:
        entry['state'] = info_list['state']
    elif 'state' in kwargs:
        entry['state'] = kwargs['state']
    else:
        entry['state'] = input('Pls enter the user state: ')

    return dict(entry)

def create_id(phone_dict:dict):
    if len(phone_dict) == 0:
        return '0'
    else:
        keys_list = [int(key) for key in phone_dict]
        for i in range(MAX_BOOK_SIZE):
            if i in keys_list:
                continue
            else:
                return str(i)

def list_instance(instance:dict, file:str = 'YOUR BOOK', **kwargs):
    print(TEXT_CYAN + '-------------> ' + file + ' <--------------' + RESET_COLORS)
    if len(kwargs) > 0:
        print(TEXT_CYAN +'SEARCH CONDITIONS -> '+ RESET_COLORS, end='')
        for k, v in kwargs.items():
            print(TEXT_CYAN + k, '=' + RESET_COLORS, v, end=' ')
        print()
    for key, value in instance.items():
        print(TEXT_CYAN + key + RESET_COLORS, ":", end= " " )
        for k, v in value.items():
            print(TEXT_ROSA + k + RESET_COLORS + ': ' + v, end= ' ')
        print()
    print(TEXT_CYAN + '-----------------------------------------' + RESET_COLORS)

def search_book(book:dict, **kwargs) -> dict | None:
    entries_list = {}
    for k in book:
        has_value = []
        for key, value in kwargs.items():
            has_value.append(True if book[k][key].lower() == value.lower() else False)

        if all(i == True for i in has_value):
            entries_list[k] = book[k]
    return entries_list if len(entries_list) > 0 else None

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if __name__ == '__main__':
    # INIT colorama
    colorama.init()

    # SET values
    phone_book = None
    file_name = DEFAULT_FILE_NAME

    # OPEN book if script open in cmd and filename argument was provided
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        phone_book = open_book(file_name, phone_book)

    # ---------------------> MAIN PROCESS LOOP <-----------------
    while True:
        # SHOW menu
        print(TEXT_YELLOW + '--->' + RESET_COLORS)
        show_menu(MAIN_MENU)
        if phone_book is not None:
            show_menu(BOOK_MENU)
        user_choice:str = input(TEXT_YELLOW + 'Pls enter your choice: '+ RESET_COLORS)
        try:
            user_choice:int = int(user_choice)
        except ValueError:
            print(TEXT_RED + '---> WRONG INPUT FORMAT... TRY AGAIN' + RESET_COLORS)
            continue
        else:
            if user_choice not in range(12):
                print(TEXT_RED + '---> NO SUCH ACTION... TRY AGAIN' + RESET_COLORS)
                continue

        # DOING some action depending on user choice
        match user_choice:
            # QUIT menu and program
            case 0:
                print(TEXT_YELLOW + '>>>>>>>>>>>>>>>>>>>>>>>>> THANK YOU FOR USING *UBM* PRODUCT <<<<<<<<<<<<<<<<<<<<<<<<<' + RESET_COLORS)
                break

            # OPEN phone_book
            case 1:
                file_name:str = input('Pls enter phonebook name: ')
                phone_book:dict = open_book(file_name, phone_book)


            # CREATE new book
            case 2:
                phone_book = {}
                file_name = input('Pls enter the name for new book(without extension)') + '.json'


                # SAVE changes to file
                save_book(file_name, phone_book)

            # SHOW phonebook
            case 3 if phone_book is not None:
                if len(phone_book) > 0:
                    list_instance(phone_book, file_name)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_CYAN + f'------------- THERE ARE NO ENTRIES YET IN YOUR PHONEBOOK ' +
                          TEXT_ROSA + file_name + TEXT_CYAN + ' ------------------' + RESET_COLORS)

            # CREATE new entry in phonebook
            case 4 if phone_book is not None:
                entry_id = create_id(phone_book)
                phone_book[entry_id] = create_entry()
                print(TEXT_ROSA + f'NEW ENTRY WAS CREATED UNDER ID {entry_id} ')

                # SAVE changes to file
                save_book(file_name, phone_book)

            # SEARCH entry by name
            case 5 if phone_book is not None:
                show_name = input('---> Pls enter the name: ')
                result = search_book(phone_book, name = show_name)
                if result:
                    list_instance(result, file_name, name = show_name)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_RED + f"---> NO USER WITH SUCH A NAME '{show_name}" + RESET_COLORS)

            # SEARCH entry by last name
            case 6 if phone_book is not None:
                show_last_name = input('---> Pls enter the last name: ')
                result = search_book(phone_book, last_name = show_last_name)
                if result:
                    list_instance(result, file_name, last_name = show_last_name)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_RED + f'---> NO USER WITH SUCH A SURNAME "{show_last_name}"' + RESET_COLORS)

            # SEARCH user by fullname
            case 7 if phone_book is not None:
                show_name = input('---> Pls enter the name: ')
                show_last_name = input('---> Pls enter the last name: ')
                result = search_book(phone_book,
                                     name = show_name,
                                     last_name = show_last_name)
                if result:
                    list_instance(result, file_name, name = show_name,
                                                     last_name = show_last_name)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_RED + f'---> NO USER WITH SUCH A FULLNAME "{show_name + ' ' + show_last_name}"' + RESET_COLORS)

            # SEARCH user by city
            case 8 if phone_book is not None:
                show_city = input('---> Pls enter the city for search: ')
                result = search_book(phone_book, city = show_city)
                if result:
                    list_instance(result, file_name, city = show_city)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_RED + f'---> NO USER WITH SUCH A CITY "{show_city}"' + RESET_COLORS)

            # SEARCH by state
            case 9 if phone_book is not None:
                show_state = input('---> Pls enter the state for search: ')
                result = search_book(phone_book, state = show_state)
                if result:
                    list_instance(result, file_name, state = show_state)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_RED + f'---> NO USER WITH SUCH A STATE "{show_state}"' + RESET_COLORS)

            # SEARCH by name, lastname, phone, city, state
            case 10 if phone_book is not None:
                show_name = input('---> Pls enter the name: ')
                show_last_name = input('---> Pls enter the last name: ')
                show_tel = input('---> Pls enter the phone number: ')
                show_city = input('---> Pls enter the city: ')
                show_state = input('---> Pls enter the state: ')
                result = search_book(phone_book,
                                     name = show_name,
                                     last_name = show_last_name,
                                     tel = show_tel,
                                     city = show_city,
                                     state = show_state)
                if result:
                    list_instance(result, file_name, name = show_name,
                                                     last_name = show_last_name,
                                                     tel = show_tel,
                                                     city = show_city,
                                                     state = show_state)
                    show_edit_menu(phone_book)
                else:
                    print(TEXT_RED + '---> NO USER WITH SUCH A COMBINATION OF ALL KEYS' + RESET_COLORS)
            # DELETE all entries
            case 11 if phone_book:
                phone_book = {}
                with open(file_name, 'w') as f_o:
                    json.dump(phone_book, f_o)

        print(TEXT_YELLOW + '>>>>>>>>>>>>>>>>>>>>>>>>> OPERATION FINISHED <<<<<<<<<<<<<<<<<<<<<<<<<' + RESET_COLORS)











