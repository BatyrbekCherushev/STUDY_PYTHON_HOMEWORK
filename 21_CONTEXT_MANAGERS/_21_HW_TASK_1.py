# 1 ====================================================================================================================
"""Task 1

File Context Manager class

Create your own class, which can behave like a built-in function 'open'. Also, you need to extend its functionality with
 counter and logging. Pay special attention to the implementation of '__exit__' method, which has to cover all the requirements to context managers mentioned here:"""
class FileCM:
    tries_counter = 0
    success_counter = 0
    """Context manager class for file handling"""
    def __init__(self, file_name, file_mode = 'r'):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file_object = None

    def __enter__(self):
        FileCM.tries_counter += 1
        print(f'START (try - {FileCM.tries_counter}) =============================================')
        print('===> STAGE-1  (__enter__) executing <===')
        try:
            print(f'   > trying to open file {self.file_name} in {self.file_mode} mode')
            self.file_object = open(self.file_name, self.file_mode)

        except FileNotFoundError as e:
            print('No such file ')
            print('!!! STAGE-3 (__exit__) will not execute')
            raise
        else:
            print(f'   > file {self.file_name} opened successfully')
            FileCM.success_counter += 1
            return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('===> STAGE-3 (__exit__) executing... <===')
        print(f'   > I opened file successfully {FileCM.success_counter} time') # ми можемо вважати успішною спробу, тому що це метод спрацьовує тільки коли успішно відпрацював метод __enter__

        # catching error in 'suite' block of with statement
        if exc_val:
            print(f'   !!! an {str(exc_val).upper()} error occurred on STAGE-2 during executing suite code block')
            print(f'   exc_type = {exc_type}, exc_value = {exc_val}, exc_traceback = {exc_tb}')

        # close file object
        if self.file_object and not self.file_object.closed:
            self.file_object.close()
        print(f'============================================= END (try - {FileCM.tries_counter})')


# # TESTING
# with FileCM('test_1.txt') as fo:
#     print('===> STAGE 2: executing inside logic <===')
#     print(f'   > printing file content:')
#     print(fo.read())
#     1 / 0
#     # x = 1 + '2'
#
# with FileCM('test_1.txt', 'a') as fo:
#     print('   > writing to file')
#     fo.write('Hello world!!!\n')

