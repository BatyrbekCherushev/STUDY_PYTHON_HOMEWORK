# -----------------------> TASK-01 <--------------------------------
def oops():
    # print([1,2,3][4])
    print({'some': 'value'}['key'])
def check_error():
    try:
        oops()
    except IndexError as err_inst:
        print('IndexError occurred')
        print(err_inst.args)
    # except Exception as err_inst:
    #     print(type(err_inst))
    #     print(err_inst.args)
    #     print(err_inst)

check_error()

"""Коли міняємо на іншу помилку, то в другій функції відловлюватись вже не буде.
Треба або додати виключення для KeyError, або загальне виключення, щоб її відловити
"""

# --------------------------------> TASK-02 <---------------------------------
def count_nums(a, b):
    try:
        num_1 = float(a)
        num_2 = float(b)
        return  (num_1 * num_1) / num_2
    except ValueError as err_inst:
        print('ValueError occurred')
        print(err_inst.args)
    except ZeroDivisionError as err_inst:
        print('ZeroDivisionError occurred')
        print(err_inst)
        print(err_inst.args)

    return None

print(count_nums(
    input('Pls, enter first number: '),
    input('Pls, enter second number: ')
))