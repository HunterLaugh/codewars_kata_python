# coding:utf-8

import unittest
import sys
sys.path.append('/mnt/f/github/codewars_kata_python')
from mathfunc import *

class TestMathFunc(unittest.TestCase):
	'''Test mathfunc.py'''
		
	def test_add(self):
		'''Test method add(a,b)'''
		self.assertEqual(3,add(1,2))
		self.assertNotEqual(3,add(2,2))
		
		
	def test_minus(self):
		'''Test method minus(a,b)'''
		self.assertEqual(1,minus(3,2))
		
		
	def test_multi(self):
		'''Test method multi(a,b)'''
		self.assertEqual(6,multi(2,3))
		
		
	def test_divide(self):
		'''Test method divide(a,b)'''
		self.assertEqual(2,divide(6,3))
		self.assertEqual(2.5,divide(5,2))
		self.assertEqual('Error',divide(3,0))
		
	
if __name__=='__main__':
	unittest.main()