'''
Split Strings
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

'''
# TEST CASE  ALL PASSED
a="asdfadsf"     # ['as', 'df', 'ad', 'sf']
b="asdfads"      #['as', 'df', 'ad', 's_']
c=""             # []
d="x"            # ["x_"]

def solution(s):
	if not s:
		return []
	
	if len(s)%2==1:
		s=s+'_'
	
	res=[]
	i=0
	n=len(s)
	while i<(n-1):
		res.append(s[i:i+2])
		i+=2
	return res
		
		

	
	
print(solution(d))