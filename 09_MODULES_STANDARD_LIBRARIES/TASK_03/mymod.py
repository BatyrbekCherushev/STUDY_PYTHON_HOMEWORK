import sys, os

def count_lines(name):
    with open(name, 'r') as fo:
        file_lines = fo.readlines()

    return len(file_lines)

def count_chars(name):
    with open(name, 'r') as fo:
        file_string = fo.read()

    return len(file_string)

def test(name):
    return count_lines(name), count_chars(name)

if __name__ == '__main__':
    file_name = sys.argv[0]

    # CHECKING if there were some arguments in command line
    arg_len = len(sys.argv)
    if arg_len >= 2 and sys.argv[1] == '--execute':
        if arg_len >= 3 and os.path.exists(sys.argv[2]):
            file_name = sys.argv[2]


    # PRINTING file info
    print(f'---> Checking {file_name}')
    print(f'---> it has...\n\t{count_chars(file_name)} characters\n\t{count_lines(file_name)} lines')


