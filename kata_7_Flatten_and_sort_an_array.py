'''
7 kyu
Flatten and sort an array
Challenge:
Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:
Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

Test case:
Test.it("should work for some simple example test cases")
test.assert_equals(flatten_and_sort([]), [])
test.assert_equals(flatten_and_sort([[], [1]]), [1])
test.assert_equals(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
test.assert_equals(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]), [1, 2, 3, 4, 5, 6, 100])

'''

def flatten_and_sort(array):
	res=[]
	for each in array:
		for item in each:
			res.append(item)
	res.sort()
	return res

# test case  --> PASSED ALL THE CASES
t1=[]
t2=[[],[1]]
t3=[[3,2,1],[7,9,8],[6,4,5]]
t4=[[1,3,5],[100],[2,4,6]]
case=[t1,t2,t3,t4]
for t in case:
	print(flatten_and_sort(t))

