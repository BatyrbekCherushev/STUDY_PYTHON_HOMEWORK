import sys

# ІМПОРТ користувацького модуля до очищення вмісту списку sys.path - все ок
#import some_lib

print(type(sys.path))
# BEFORE CHANGES
for path in sys.path:
    print(path)

#CHANGES in sys.path
sys.path = []

# AFTER CHANGES
print(sys.path)

#ІМПОРТ модлуів після зміни - для юзер-модуля кидає включення ModuleNotFoundError: No module named 'some_lib'
#Для вбудованого модуля без змін - нормально імпортує
import os
print(os.getcwd())

import some_lib






