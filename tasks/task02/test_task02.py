import unittest
import task02

class Test02Test(unittest.TestCase):

    def test_string_3_6(self):

        self.assertEqual(task02.string_3_6('123456789123456789'),'369369')