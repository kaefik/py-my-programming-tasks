import unittest
import task01


class Task01Test(unittest.TestCase):
    """ проверяем решение первой задачи """

    def test_print_three_simbol_a(self):
        self.assertEqual(task01.print_three_simbol('a'), 'bcd')

    def test_print_three_simbol_z(self):
        self.assertEqual(task01.print_three_simbol('z'), 'abc')
