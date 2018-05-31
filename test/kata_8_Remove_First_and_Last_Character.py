'''
8 kyu
Remove First and Last Character
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, except in C, where, to keep the difficulty at the level of the kata, you are given two parameters, the first a buffer with length exactly the same as the second parameter, the original string. You don't have to worry with strings with less than two characters.
'''

def remove_char(s):
	li_s=list(s)
	li_s.pop()
	li_s.pop(0)
	res=''.join(li_s)
	
	return res

