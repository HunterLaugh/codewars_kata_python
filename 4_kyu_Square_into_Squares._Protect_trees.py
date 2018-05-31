'''
My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.
Task

Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return the result with the largest possible values:
Examples

decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.
Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift).

The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

[x1 ... xk]

Note for Bash

decompose 50 returns "1,3,5,8,49"
decompose 4  returns "Nothing"

Hint

Very often xk will be n-1.

'''
# 输入 n ，输出序列m ，序列m满足条件 n**2=m[0]**2+m[1]**2+...，即序列m的平方和等n的平方，且m为递增序列，取最大的值
def decompose(n):
	sum=n**2
	m=[]
	while sum-m[-1]**2 !=0:
		for i in range(n-1,0,-1):
			