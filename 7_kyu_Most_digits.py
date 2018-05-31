'''
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
'''

def find_longest(arr):
	longest=arr[0]
	for each in arr[1:]:
		if len(str(each))>len(str(longest)):
			longest=each
	return longest
			

# TEST CASE	PASSED ALL THE CASE
find_longest([1, 10, 100])				# 100
find_longest([9000, 8, 800])			# 9000
find_longest([8, 900, 500])				# 900
find_longest([3, 40000, 100])			# 40000
find_longest([1, 200, 100000])			# 100000