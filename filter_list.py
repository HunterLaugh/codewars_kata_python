"""
List Filtering

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
#  use type(l[n])
#  list.pop(i)    remove  str

def filter_list(L):
	num=[]
	for x in L:
		if type(x)==int:
			num.append(x)		
	return num

print(filter_list([1,2,'a','b','c',3]))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))