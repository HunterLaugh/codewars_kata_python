'''
The nth smallest integer
Given a list of integers, return the nth smallest integer in the list. Only distinct elements should be considered when calculating the answer. n will always be positive (n > 0)

If the nth small integer doesn't exist, return None

Note: "indexing" starts from 1
Examples

[1, 3, 4, 5], 7        ==> None  # n is more than the size of the list
[4, 3, 4, 5], 4        ==> None  # 4th smallest integer doesn't exist
[45, -10, 4, 5, 4], 4  ==> 45    # 4th smallest integer is 45

Time is an essence. Focus on efficiency.

If you get a timeout, just try to resubmit your solution. However, if you always get a timeout, review your code.

'''
def nth_smallest(arr, n):
	a=set(arr)
	b=list(a)
	b.sort()
	try:
		return b[-n]
	except IndexError:
		return None


# TEST CAS
print(nth_smallest([14, 12, 46, 34, 334], 3))     # >>> 34
l = [455555, 2222222, 3333333, 9879799, 79977979, 79977979, 79977979, 79977979, 79977979, 79977979, 79977979, 79977979]
print(nth_smallest(l, 3))           # >>>  3333333
print(nth_smallest(l, 6))           # >>>  None)