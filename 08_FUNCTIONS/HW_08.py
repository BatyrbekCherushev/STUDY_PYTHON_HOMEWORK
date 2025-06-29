#Task-01
print('---------------> TASK-01 <---------------')

def favorite_movie(movie_name):
    print(f'My favorite movie is named {movie_name}')

favorite_movie('"Fighting club"')

#Task-02
print('\n---------------> TASK-02 <---------------')

def make_country(**kwargs):
    return {country: capital for country, capital in kwargs.items()}

print(make_country(Ukraine = 'Kyiv', German = 'Berlin'))

#Task-03
print('\n---------------> TASK-03 <---------------')

def make_operation(operation, *args):
    match operation:
        case '+':
            total = None
            for i in args:
                total = i if total is None else total + i
            return total
        case '-':
            total = None
            for i in args:
                total = i if total is None else total - i
            return total
        case '*':
            total = None
            for i in args:
                total = i if total is None else total * i
            return total
        case _:
            print('You have entered unknown operation...')

print(make_operation('*', 7, 6))

