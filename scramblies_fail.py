"""
Scramblies

Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
"""

# coding:utf-8
# str1 重排列能匹配 str2 　return True  otherwise reutrn False
# 性能考虑　<12000ms

def scramble(str1,str2):
	str1Set=set(list(str1))
	str2Set=set(list(str2))
	
	if str1Set&str2Set==str2Set:
		return True
	else:
		return False
		
print(scramble('cedewaraaossoqqyt','codewars'))
