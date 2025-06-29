with open('myfile.txt', 'w') as fo:
    fo.write('Hello, world!!!\n')

with open('myfile.txt', 'r') as fo:
    print(fo.read())

# with open('../myfile.txt', 'r') as fo:
#     print(fo.read())

"""З командної строки працює. Новий файл виникає."""

"""Якщо вказати інгий шлях для відкривання файла, то викидає помилку:
 FileNotFoundError: [Errno 2] No such file or directory: '../myfile.txt'"""

