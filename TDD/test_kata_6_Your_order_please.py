import unittest
import sys
sys.path.append('/mnt/f/github/codewars_kata_python')

from kata_6_Your_order_please import *

class test_Your_order(unittest.TestCase):
	def test(self):
		self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
		self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
		self.assertEqual(order("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"), "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor")
		self.assertEqual(order(""), "")
		self.assertEqual(order("3 6 4 2 8 7 5 1 9"), "1 2 3 4 5 6 7 8 9")
		

if __name__=='__main__':
	unittest.main()