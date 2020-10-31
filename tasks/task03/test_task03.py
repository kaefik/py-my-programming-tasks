import unittest
import task03


class Task03Test(unittest.TestCase):

    def test_del_abc_number(self):
        self.assertEqual(task03.del_abc_number('fdfdsfsabc232werewhgfhfgabcjrewiewhfiabcejfedfhabc'),
                         'fdfdsfs232werewhgfhfgabcjrewiewhfiabcejfedfhabc')

    def test_del_abc_number_nodel(self):
        self.assertEqual(task03.del_abc_number('fdfdsfsabcwerewhgfhfgabcjrewiewhfiabcejfedfhabc'),
                         'fdfdsfsabcwerewhgfhfgabcjrewiewhfiabcejfedfhabc')
