"""Task 2

Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use cases
 as you can, positive ones when a file exists and everything works as designed. And also, write tests when your class raises errors or you have errors in the runtime context suite."""
import unittest
from _21_HW_TASK_1 import FileCM

class FileCMTestCase(unittest.TestCase):
    def test_opening_file(self):
        with self.assertRaises(FileNotFoundError):
            with FileCM('das'):
                pass

        with self.assertRaises(ZeroDivisionError):
            with FileCM('test_1.txt'):
                1 / 0

    # цей тесткейс підказав ШІ
    def test_success_counters(self):
        # Перевірка лічильників
        initial_tries = FileCM.tries_counter
        initial_success = FileCM.success_counter

        try:
            with FileCM("non_existing_file.txt"):
                pass
        except FileNotFoundError:
            pass

        with FileCM("test_1.txt"):
            pass

        self.assertEqual(FileCM.tries_counter, initial_tries + 2)
        self.assertEqual(FileCM.success_counter, initial_success + 1)

    # цей тесткейс підказав ШІ
    def test_file_closed_after_with(self):
        cm = FileCM("test_1.txt")
        with cm as f:
            f.read()
        # Перевіряємо, що файл закритий після виходу з with
        self.assertTrue(f.closed, "Файл має бути закритий після виходу з with")