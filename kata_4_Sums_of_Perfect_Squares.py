'''
Sums of Perfect Squares
The task is simply stated. Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n. Come up with the best algorithm you can; you'll need it!

Examples:

    sum_of_squares(17) = 2
    17 = 16 + 1 (4 and 1 are perfect squares).
    sum_of_squares(15) = 4
    15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
    sum_of_squares(16) = 1
    16 itself is a perfect square.

Time constraints:

5 easy (sample) test cases: n < 20

5 harder test cases: 1000 < n < 15000

5 maximally hard test cases: 5 * 108 < n < 109

15 random maximally hard test cases: 108 < n < 109

'''

def sum_of_squares(n):
	count=0
	while True:
		number=int(n**0.5)
		if number**2==n:
			count+=1
			return count
		else:
			n=n-number**2
			count+=1

	
print(sum_of_squares(17))
print(sum_of_squares(16))