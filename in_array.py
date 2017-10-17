"""
Which are in?
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []

#Notes: Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

Beware: r must be without duplicates.
"""

def in_array(array1,array2):
	li=[]
	for x in array1:
		for y in array2:
			if (x in y)  and  (x not in li):
				li.append(x)
	# 排序 list.sort()
	li.sort()
	return li
	
a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1,a2))
