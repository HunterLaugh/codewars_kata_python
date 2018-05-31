# coding:utf-8

import unittest
import sys
sys.path.append('/mnt/f/github/codewars_kata_python')
from 4 kyu Great Total Additions of All Possible Arrays from a List import *

class TestFunc(unittest.TestCase):
	def test_gta(self):
		self.assertEqual(328804,gta(7, 123489, 5, 67))
		self.assertNotEqual(3836040,gta(8, 12348, 47, 3639))

		
if __name__=='__main__':
	unittest.main()