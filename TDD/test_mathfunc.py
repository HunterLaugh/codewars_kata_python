# coding:utf-8

import unittest
import sys
sys.path.append('/mnt/f/github/codewars_kata_python')
from mathfunc import *

class TestMathFunc(unittest.TestCase):
	'''Test mathfunc.py'''
		
	def test(self):
		self.assertEqual(3,add(1,2))
		self.assertNotEqual(3,add(2,2))
		self.assertEqual(1,minus(3,2))
		self.assertEqual(6,multi(2,3))
		self.assertEqual(2,divide(6,3))
		self.assertEqual(2.5,divide(5,2))
		self.assertEqual(3,divide(3,1))
		
	
if __name__=='__main__':
	unittest.main()