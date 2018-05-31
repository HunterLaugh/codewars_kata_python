# coding:utf-8
# 预设过滤器A，传入数组B，返回数组C（不包含A中元素的B，保持原有顺序）
'''
8 kyu 
Filter out the geese
Write a function, gooseFilter/goose_filter/GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

For example, if this array were passed as an argument:

["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.
'''

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
	res=[]
	for each in birds:
		if each not in geese:
			res.append(each)
			
	return res
	
	
	