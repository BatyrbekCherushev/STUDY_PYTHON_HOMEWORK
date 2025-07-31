#========================================================= HW-1 ========================================================
"""School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
 and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
 and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
 should only be available to the teacher. """
class Person:
    def __init__(self, full_name, category, birth_date, location, phone, email):
        self.full_name = full_name
        self.category = category
        self.birth_date = birth_date
        self.location = location
        self.phone = phone
        self.email = email

    def show_info(self):
        print('='*10 + f' SHOWING INFO FOR {self.full_name} ' + '='*10)
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


class Student(Person):
    def __init__(self, full_name, category, birth_date, location, phone, email, study_year, teachers_list: list, disciplines_list: list):
        super().__init__(full_name, category, birth_date, location, phone, email)
        self.study_year = study_year
        self.teachers_list = teachers_list
        self.disciplines_list = disciplines_list

    def show_teachers_info(self):
        print('='*10 + f" SHOWING INFO OF TEACHERS FOR STUDENT {self.full_name} " + '='*10)
        for teacher in self.teachers_list:
            teacher.show_info()


class Teacher(Person):
    def __init__(self, full_name = '', category = '', birth_date = '', location = ' ', phone = ' ',
                 email = ' ', salary_basic = 0, teaching_years = 0, discipline = ' ',
                 is_curator = False, students_list = []):
        super().__init__(full_name, category, birth_date, location, phone, email)
        self.salary_basic = salary_basic
        self.discipline = discipline
        self.is_curator = is_curator
        self.teaching_years = teaching_years
        self.salary_full = salary_basic + salary_basic * .3 * (self.teaching_years // 10)
        self.students_list = students_list

    def get_salaries(self):
        return self.salary_basic, self.salary_full

teacher_1 = Teacher(category='TEACHER',
                    full_name = 'Archimedus')
teacher_2 = Teacher(category = 'TEACHER',
                    full_name = 'Billy Bob Thornton',
                    birth_date = '1976.09.4',
                    salary_basic = 3000,
                    teaching_years = 21)

student_1 = Student('Cherushev Batyrbek',
                    'STUDENT',
                    '9.10.1985',
                    'Kyiv',
                    '+3806373939',
                    'ifenk@gmail.com',
                    3,
                    [teacher_1, teacher_2],
                    ['CS50', 'PYTHON', 'Embedded developing', 'Game developing'])

# # TESTING
# student_1.show_info()
# student_1.show_teachers_info()
# # teacher_1.show_info()
# print(teacher_2.get_salaries())

#========================================================= HW-2 ========================================================
"""Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'"""
import calendar
class Mathematician:
    @staticmethod
    def square_nums( some_list: list):
        return [i * i for i in some_list]

    @staticmethod
    def remove_positives(some_list:list):
        # return list(filter(lambda  x: x < 0, some_list))
        return [x for x in some_list if x < 0]

    @staticmethod
    def filter_leaps(some_list):
        return [year for year in some_list if calendar.isleap(year)]

# TESTING
m = Mathematician()
print(m.square_nums([1,2,3]))
print(m.remove_positives([2,3,-4,45,-4,-5,3,4,5]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

#========================================================= HW-3 ========================================================
"""Task 3

Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional 
classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers 
(type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. 
It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store."""

class Product:
    def __init__(self, prod_type, name, price):
        self.prod_type = prod_type
        self.name = name
        self.basic_price = price

class WarehouseProduct:
    def __init__(self, name, product_type, amount, basic_price, current_price):
        self.name = name
        self.type = product_type
        self.amount = amount
        self.basic_price = basic_price
        self.current_price = current_price
        self.discount = 0

class Warehouse:
    def __init__(self):
        self.products_list = []
        self.categories = []

    def add_product(self, product, amount,  real_price):
        self.products_list.append(WarehouseProduct(name = product.name,
                                                   product_type = product.prod_type,
                                                   amount = amount,
                                                   basic_price = product.basic_price,
                                                   current_price = real_price))

    def get_categories(self):
        result = set()
        for product in self.products_list:
            result.add(product.type)
        return result

    def find_product_index(self, product_name):
        for i in range(len(self.products_list)):
            if self.products_list[i].name == product_name:
                return i
        return False

class ProductStore:

    def __init__(self, price_premium):
        self.warehouse = Warehouse()
        self.price_premium = price_premium
        self.discount = 0
        self.income = 0


    def add(self, product, amount):
        self.warehouse.add_product(product, amount, product.basic_price + product.basic_price * self.price_premium)

    def get_product_info(self, product_name):
        result = self.warehouse.find_product_index(product_name)
        if result != False:
            return self.warehouse.products_list[result].__dict__
        else:
            raise Exception('No such product in warehouse')

    def show_products_types(self):
        print(self.warehouse.get_categories())

    def sell_product(self, product_name, amount):
        prod_id = self.warehouse.find_product_index(product_name)
        if prod_id != False:
            product = self.warehouse.products_list[prod_id]
            if (product.amount - amount) >= 0:
                self.income += product.current_price * amount
                product.amount -= amount
                print(f"There was sold {amount} units of {product.name}. Price was {product.current_price}. Now your income is {self.income}. We have {str(product.amount) +' '+ product_name} in warehouse left")
            else:
                raise Exception(f'No such amount of {product.name}. We have only {product.amount} of it in our warehouse')

    def set_discount(self, identifier, percent, identifier_type = 'name'):
        for product in self.warehouse.products_list:
            searched_product = None
            if identifier_type == 'name' and product.name == identifier:
                searched_product = product
            elif identifier_type == 'type' and product.type == identifier:
                searched_product = product
            if searched_product is not None:
                searched_product.discount = percent / 100
                basic_price = searched_product.basic_price
                current_price = basic_price + basic_price * self.price_premium
                searched_product.current_price = current_price - current_price * searched_product.discount

    def get_income(self):
        return self.income
    def get_all_products(self):
        result = []
        for product in self.warehouse.products_list:
            result.append(product.__dict__)
        return result


            # TESTING

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore(.3)
s.add(p, 10)
s.add(p2, 300)
#
# #TESTING
# # print(s.warehouse.products_list)
# print(s.get_product_info('Ramen'))
# s.show_products_types()
# s.sell_product('Ramen', 300)
# print(s.get_product_info('Ramen'))
# s.set_discount('Ramen', 50
#                )
# print(s.get_product_info('Ramen'))
# print(s.get_all_products())

#========================================================= HW-4 ========================================================
"""Custom exception

Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its functionality
 to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving messages to file"""
class CustomException(Exception):
    """My custom exception"""

    log_file_name = 'logs.txt'

    def __init__(self, *args):
        super().__init__(*args)
        print(self.args)
        with open(self.log_file_name, 'a') as fo:
            fo.write(f"CustomExceptionError: {str(self.args)} \n")


try:
    raise  CustomException('Some new error',410,5)
except CustomException as e:
    print(e.args)