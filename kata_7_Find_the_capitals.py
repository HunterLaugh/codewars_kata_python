'''
Find the capitals
Instructions

Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
Example

Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

'''
def capitals(word):
	res=[]
	index=0
	while index<len(word):
		if word[index].isupper():
			res.append(index)
		index+=1
	return res

# TEST CASE	PASSED ALL THE CASES
 capitals('CodEWaRs')		#	[0,3,4,6]