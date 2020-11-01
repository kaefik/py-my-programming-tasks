import unittest
import task04


class Task04Test(unittest.TestCase):

    def setUp(self) -> None:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        number = '0123456789'
        spec_simbol = '~`!@$%^&*(){}<>'
        self.abc_pass = abc + number + spec_simbol

    def test_is_my_password_yes(self):
        self.assertEqual(task04.is_my_password('WsE}t68Kg@(U'), True)

    def test_is_my_password_no(self):
        self.assertEqual(task04.is_my_password('Wse}t68Kg@(U'), False)

    def test_is_my_password_generate(self):
        pswrd = task04.generate_password(self.abc_pass, 20)
        self.assertEqual(task04.is_my_password(pswrd), True)
