import unittest, json
from testing_example import TVController
from phonebook import search_book, create_id
# 1 ====================================================================================================================
"""Task 1

Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library. """
class TVControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.test_controller = TVController(["BBC", "Discovery", "TV1000"])

    def test_turn_channel(self):
        self.assertEqual(self.test_controller.current_channel(), 'BBC')
        self.assertEqual(self.test_controller.last_channel(), 'TV1000')
        self.assertEqual(self.test_controller.turn_channel(-1), 'BBC')
        self.assertEqual(self.test_controller.turn_channel(100000), 'BBC')
        self.assertEqual(self.test_controller.turn_channel(2), 'Discovery')

    def test_channel_existing(self):
        self.assertEqual(self.test_controller.exists(4), 'No')
        self.assertEqual(self.test_controller.exists(0), 'No')
        self.assertEqual(self.test_controller.exists(1), 'Yes')
        self.assertEqual(self.test_controller.exists("Discovery"), 'Yes')
        self.assertEqual(self.test_controller.exists("BBC"), 'Yes')

# 2 ====================================================================================================================
"""Task 2

Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and write tests using unittest library"""

TEST_BOOK_NAME = 'test_book.json'

class PhonebookTestCase(unittest.TestCase):
    def setUp(self, ):
        with open(TEST_BOOK_NAME,'r') as f_o:
            self.test_book = json.load(f_o)

    def test_search(self):
        self.assertEqual(search_book(self.test_book, last_name = 'bugi-wugi'), None)
        self.assertEqual(json.dumps(search_book(self.test_book, name='Batyr')), json.dumps({
            '0': {'name': 'Batyr', 'last_name': 'Cherushev', 'tel': '+3098908435', 'city': 'Kyiv', 'state': 'Kyivska oblast'}}))
        self.assertEqual(json.dumps(search_book(self.test_book, city = 'Tilimilytryandiya')), json.dumps({"1": {
        "name": "Goga",
        "last_name": "Bumz",
        "tel": "000",
        "city": "Tilimilytryandiya",
        "state": "Land of fools"
    }}))

    def test_id_creating(self):
        self.assertNotEqual(create_id(self.test_book), 2)
        self.assertEqual(create_id(self.test_book), '2')
        self.assertNotEqual(create_id({}),1)
        self.assertNotEqual(create_id({}), 0)
        self.assertEqual(create_id({}), '0')