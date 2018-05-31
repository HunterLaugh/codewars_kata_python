# coding:utf-8
'''
6 kyu
Sub-array division

In this Kata, you will be given an array of numbers and a number n, and your task will be to determine if any array elements, when summed (or taken individually), are divisible by n.

For example:

    solve([1,3,4,7,6],9) = True, because 3 + 6 is divisible by 9; solve([1,2,3,4,5],10) = True for similar reasons.

    solve([8,5,3,9],7) = True), because 7 evenly divides 5 + 9, but solve([8,5,3],7) = False.

More examples in the test cases.

Good luck!
'''

# 求数组的所有组合，如取1个，取2个，取3个...
# if 组合和%n==0  return True  else return False
def solve(arr,n):
	flag=False
	while i>=len(arr):
		
	
