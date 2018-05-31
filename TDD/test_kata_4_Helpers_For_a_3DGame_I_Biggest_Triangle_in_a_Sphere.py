# coding:utf-8

import unittest
import sys
sys.path.append('/mnt/f/github/codewars_kata_python')
from kata_4_Helpers_For_a_3DGame_I_Biggest_Triangle_in_a_Sphere import *

class Test_biggest_triang_int(unittest.TestCase):
	'''Test mathfunc.py'''
		
	def test(self):
		points_list1 = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
		sphere_center1 = [1, 2, -2]
		radius1 = 8
		res = biggest_triang_int(points_list1, sphere_center1, radius1)
		result = [4, 22.627416997969508, [[1, 2, -4], [2, 3, 5], [-2, -1, 1]]]
		self.assertEqual(res[0], result[0])
		self.assertEqual(res[2], result[2])
		self.assertEqual(res[1], result[1])

		points_list2 = [[1,2,-4],[-3, 2, 4],[7, 8, -4],
		[2, 3, 5],[-2, -1, 1],[3, 2, 6],[1, 4, 0], 
		[-4, -5, -6],[4, 5, 6],[-2, -3, -5],[-1, -2, 4],
		[-3, -2, -6], [-1, -4, 0], [2, 1, -1]]
		sphere_center2 = [0, 0, 0]
		radius2 = 8
		res2 = biggest_triang_int(points_list2, sphere_center2, radius2)
		result2 = [165, 33.645207682521445, 
		[[[1, 2, -4], [3, 2, 6], [-1, -4, 0]], 
		[[1, 4, 0], [-1, -2, 4], [-3, -2, -6]]]]
		self.assertEqual(res2[0], result2[0])
		self.assertEqual(res2[2], result2[2])
		self.assertEqual(res2[1], result2[1])
		
	
if __name__=='__main__':
	unittest.main()