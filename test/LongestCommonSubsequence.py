'''
Longest Common Subsequence

lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"

Notes

    Both arguments will be strings
    Return value must be a string
    Return an empty string if there exists no common subsequence
    Both arguments will have one or more characters (in JavaScript)
    All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ), which would have two possible longest common subsequences: "12" and "34".

Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.

Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest common subsequence will be valid).
Tips

Wikipedia has an explanation of the two properties that can be used to solve the problem:

    First property
    Second property

'''


'''
 解题思路
 string 转 set 去除重复项
 set 求交集 & 得到子集
 此路不通，set得到集合无序，导致最后得到的subsequence和预期的不同 
def lcs(x, y):
	setX=set(list(x))
	setY=set(list(y))
	print('setX: ',setX,'setY: ',setY)
	subXY=setX&setY
	subXY=list(subXY)
	subXY=''.join(subXY)
	print(subXY)
	return subXY
	
lcs('abcdef','abc')
'''

def lcs(x, y):
	if len(x)<=len(y):
		min=x
		max=y
	else:
		min=y 
		max=x
	
	re=[]
	for each in list(min):
		if each in max:
			if each not in re:
				re.append(each)
				
	res=''.join(re)	
			
	return res
	
print(lcs('abcdef','abc'))
print(lcs('a','bc'))