import unittest
import task05


class Task05Test(unittest.TestCase):

    def test_cut_only_filename_v1(self):
        self.assertEqual(task05.cut_only_filename('c:\WebServers\home\testsite\www\myfile.txt'),
                         'myfile')

    def test_cut_only_filename_v2(self):
        self.assertEqual(task05.cut_only_filename('c:\WebServers\home\testsite\www\myfile'),
                         'myfile')

    def test_cut_only_filename_v3(self):
        self.assertEqual(task05.cut_only_filename('myfile'), 'myfile')