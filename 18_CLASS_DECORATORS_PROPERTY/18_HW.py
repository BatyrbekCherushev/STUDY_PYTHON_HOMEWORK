# =================================================== 1 ================================================================
"""Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is
a valid email string."""
class TestClass:
    ALLOWED_EMAIL_PREFIX_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+/=?^_`{|}~.-"
    DOMAIN_VALID_SYMBOLS = ALLOWED_EMAIL_DOMAIN_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."

    def __init__(self, email):
        self.email = email

    @classmethod
    def validate_email(cls, email: str):
        if cls.is_email_valid(email):
            return cls(email)
        else:
            raise ValueError('Email string provided is not valid...')

    @staticmethod
    def is_email_valid(email: str):
        if not isinstance(email, str):
            return False
        if email.count('@') != 1:
            return False
        # mycode - 1
        # split_email_str = email.split('@')
        # if len(split_email_str) == 2:
        #     prefix = split_email_str[0]
        #     domain = split_email_str[1]

        # mycode - 1 - AI refactored
        prefix, domain = email.split('@')

        # mycode-2
        # if TestClass.is_domain_valid(domain) and TestClass.is_prefix_valid(prefix):
        #     return True
        # else:
        #     return False

        #my code-2 AI refactored
        if not prefix or not domain:
            return False

        if not TestClass.is_prefix_valid(prefix):
            return False

        if not TestClass.is_domain_valid(domain):
            return False

        return True

    @staticmethod
    def is_prefix_valid(prefix: str):
        if (prefix.startswith('.') or
                prefix.endswith('.') or
                '..' in prefix):
            return False
        if (prefix.startswith('-') or
                prefix.endswith('-')):
            return False
        for character in prefix:
            if not character in TestClass.ALLOWED_EMAIL_PREFIX_CHARS:
                return False
        return True

    @staticmethod
    def is_domain_valid(domain: str):
        if (domain.startswith('.') or
                domain.endswith('.') or
                '..' in domain):
            return False
        if (domain.startswith('-') or
                 domain.endswith('-') or
                 '--' in domain):
            return False
        domain_parts = domain.split('.')
        for part in domain_parts:
            if part.startswith('-') or part.endswith('-'):
                return False

        for character in domain:
            if character not in TestClass.ALLOWED_EMAIL_DOMAIN_CHARS:
                return False
        return True


# =================================================== 2 ================================================================
"""Task 2

Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
 You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances 
 of Worker class to workers list directly via access to attribute, use getters and setters instead!

You can refactor the existing code."""


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.__workers = []

    @property
    def workers(self):
        return self.__workers.copy()

    def add_worker(self, new_worker):
        if not isinstance(new_worker, Worker):
            raise TypeError('Can only add Worker instances.')

        if not new_worker in self.__workers:
            self.__workers.append(new_worker)
            if new_worker.boss is not self:
                new_worker.boss = self

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError('New boss instance has to be of class Boss...')
        if not new_boss is self._boss:
            self._boss = new_boss

            if self not in new_boss.workers:
                new_boss.add_worker(self)

#TESTING
# boss_1 = Boss(0, 'Boris', 'IBM')
#
# worker = Worker(0, 'Goga', 'IBM', boss_1)
#
# boss_1.add_worker(Worker(1, 'f','fdas', boss_1))
# print(boss_1.workers)

# =================================================== 3 ================================================================
"""Task 3

Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):

methods:

to_int

to_str

to_bool

to_float

Don't forget to use @wraps"""

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(value):
            try:
                return int(func(value))
            except (ValueError, TypeError):
                raise ValueError('Function return value is not convertible to int... ')
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(value):
            try:
                return float(func(value))
            except (ValueError, TypeError):
                raise ValueError('Function return value is not convertible to float... ')
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(value):
            return str(func(value))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(value):
            return bool(func(value))
        return wrapper
#
# # -----------> TESTING
# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string
#
#
# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string
#
#
# assert do_nothing('25') == 25
#
# assert do_something('True') is True

