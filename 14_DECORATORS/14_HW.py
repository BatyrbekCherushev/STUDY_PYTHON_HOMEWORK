from functools import wraps

# ===============================================> TASK-01 <============================================================
"""Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!"""

def logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f'---> {f.__name__} was called with...\n{'---> args: ' + str(args) + '\n'  if args else '---> no args\n'}'
              f'{'---> kwargs: ' + str(kwargs) if kwargs else '---> no kwargs '}')
        return f(*args, **kwargs)

    return wrapper

@logger
def some_func(*args, **kwargs):
    print('I am target function')

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

# ===============================================> TASK-02 <============================================================
"""Write a decorator that takes a list of stop words and replaces them with * inside the decorated function"""
def stop_words(stop_words_list):
    def decorate_f(f):
        @wraps(f)
        def wrapper(*args):
            result_string = f(*args)
            for word in stop_words_list:
                result_string = result_string.replace(word, '*')
            return result_string
        return wrapper
    return decorate_f

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

# ===============================================> TASK-03 <============================================================
"""
Write a decorator 'arg_rules' that validates arguments passed to the function.
A decorator should take 3 arguments:

max_length: 15
type_: str
contains: []  - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
"""
def arg_rules(type_: type, max_length: int, contains: list):
    def decorate_f(f):
        @wraps(f)
        def wrapper(name):
            error_list = []
            if type(name) is not type_:
                error_list.append(f'>>> Wrong type, must be { type_}')
            else:
                if len(name) > max_length:
                    error_list.append(f'>>> Wrong length, max is {max_length}')
                if not all(part in name for part in contains):
                    error_list.append(f'>>> Argument doesn`t contain all essential parts, must have {contains}')

            if len(error_list) == 0:
                return f(name)
            else:
                print('---> INVALID ARGUMENT: ')
                for error in error_list:
                    print(error)
                return False
        return wrapper
    return decorate_f

@arg_rules(type_ = str, max_length = 15, contains = ['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"