#============================================================ 1 ========================================================
"""Task 1

Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses:
Dog and Cat, and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.  """


class Animal:
    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        print('Woof, woof...')


class Cat(Animal):
    def talk(self):
        print('Meoww...')

def make_animal_talk(animal):
    animal.talk()

# --------------> TESTING
# make_animal_talk(Cat())
# make_animal_talk(Dog())

#============================================================ 2 ========================================================
"""Task 2

Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books"""
class Author:
    def __init__(self, name, country, birthday, books = None):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books if books is not None else []

    def __str__(self):
        return (f"---> Information about author...\nName: {self.name}\nCountry: {self.country}\n"
                f"Birthday: {self.birthday}\nBooks: {[f"{book.name} ({book.year})" for book in self.books]}")

    def __repr__(self):
        return f"Name: {self.name}"


class Book:
    books_count = 0

    def __init__(self, name, year: int, author:Author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.books_count += 1

    def __str__(self):
        return f"---> Book information...\nName: {self.name}\nAuthor: {self.author.name}\nYear: {self.year}"

    def __repr__(self):
        return f" {self.name} ({self.year})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return (f"Information about LIBRARY...\nName: {self.name}\nBooks: {[book for book in self.books]}\n"
                f"Authors: {[author for author in self.authors]}")

    def new_book(self, name: str, year: int, author: Author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        if not author in self.authors:
            self.authors.append(author)
        return new_book

    def get_author_by_name(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        return None

    def get_book_by_name(self, book_name):
        for book in self.books:
            if book.name == book_name:
                return book
        return None

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

a1 = Author("Брати Стругацькі", "СРСР", "1933-11-15")
a2 = Author("Тері Пратчетт", "Велика Британія", "1948-04-28")

lib = Library("Наукова бібліотека")

lib.new_book("Пікнік на узбіччі", 1972, a1)
lib.new_book("Трудно бути богом", 1964, a1)
lib.new_book("Патруль часу", 1995, a2)


# --------------> TESTING
# print(a1.name)
# print(a1.books)
# print(lib.group_by_author(lib.get_author_by_name('Брати Стругацькі')), sep = '\n')
# print(* lib.group_by_year(1964), sep = '\n')
# print(Book.books_count)
# for book in a1.books:
#     print(book.name)
# print(a1)
# print(a2)
# print(lib)
# print(lib.get_book_by_name("Пікнік на узбіччі"
#                            ))

#============================================================ 3 ========================================================
"""Task 3

Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною
 перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction"""
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """метод що реалізує додавання двох об'єктів дробів і повертає новий об'єкт дробу"""
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        d = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // d, new_denominator // d)

    def __sub__(self, other):
        """метод реалізує віднімання двох дробів і як результат повертає новий об'єкт дробу"""
        new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        d = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // d, new_denominator // d)

    def __mul__(self, other):
        """метод реалізує множення двох об'єктів-дробів і повертає як результат новий об'єкт-дріб"""
        new_numerator = self._numerator * other._numerator
        new_denominator = self._denominator * other._denominator
        d = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // d, new_denominator // d)


    def __truediv__(self, other):
        """метод реалізує ділення двох об'єктів дробів і повертає як результат новий об'єкт-дріб"""
        new_numerator = self._numerator * other._denominator
        new_denominator = self._denominator * other._numerator
        d = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // d, new_denominator // d)

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        if type(value) != int:
            raise TypeError('Numerator cannot be float type, but int')
        else:
            self._numerator = value

    @property
    def denominator(self):
        return self._denominator


    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError('Denominator cannot be equal 0')
        elif type(value) != int:
            raise TypeError('Denominator cannot be float type, but int')
        else:
            self._denominator = value


# ------------> TESTING
# def test_fraction_operations():
#     # створення
#     f1 = Fraction(3, 4)
#     assert str(f1) == "3/4"
#
#     # додавання
#     f2 = Fraction(1, 2)
#     f3 = Fraction(1, 3)
#     assert str(f2 + f3) == "5/6"
#
#     # віднімання
#     f4 = Fraction(3, 4)
#     f5 = Fraction(1, 4)
#     assert str(f4 - f5) == "1/2"
#
#     # множення
#     f6 = Fraction(2, 3)
#     f7 = Fraction(3, 4)
#     assert str(f6 * f7) == "1/2"
#
#     # ділення
#     f8 = Fraction(3, 4)
#     f9 = Fraction(2, 3)
#     assert str(f8 / f9) == "9/8"
#
#     # спрощення
#     f10 = Fraction(2, 4)
#     f11 = Fraction(2, 4)
#     assert str(f10 + f11) == "1/1"
#
#     # помилки
#     # import pytest
#     import builtins
#
#     try:
#         Fraction(1.5, 2)
#         assert False, "TypeError for float numerator expected"
#     except TypeError:
#         pass
#
#     try:
#         Fraction(1, 0)
#         assert False, "ValueError for zero denominator expected"
#     except ValueError:
#         pass
#
#     try:
#         Fraction(1, 2.5)
#         assert False, "TypeError for float denominator expected"
#     except TypeError:
#         pass
#
# test_fraction_operations()
# print("Усі тести пройшли успішно!")












