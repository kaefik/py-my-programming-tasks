import unittest
import task07


class Task07Test(unittest.TestCase):

    def test_add_space_to_number_7(self):
        self.assertEqual(task07.add_space_to_number(1234567), '1 234 567')

    def test_add_space_to_number_6(self):
        self.assertEqual(task07.add_space_to_number(234567), '234 567')

    def test_add_space_to_number_5(self):
        self.assertEqual(task07.add_space_to_number(23456), '23 456')

    def test_add_space_to_number_3(self):
        self.assertEqual(task07.add_space_to_number(456), '456')

