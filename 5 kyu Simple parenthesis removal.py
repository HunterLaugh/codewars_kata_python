'''
Simple parenthesis removal
In this Kata, you will be given a mathematical string and your task will be to remove all braces as follows:

solve("x-(y+z)") = "x-y-z"
solve("x-(y-z)") = "x-y+z"
solve("u-(v-w-(x+y))-z") = "u-v+w+x+y-z"
solve("x-(-y-z)") = "x+y+z"

There are no spaces in the expression. Only two operators are given: "+" or "-".

More examples in test cases.

Good luck!
'''

# pass all the test case in codewars

def solve(s):
	lst_s=list(s)

	while ')' in lst_s:
		index=lst_s.index(')')
		for i in range(index-1,-1,-1):
			if lst_s[i]=='(':
				break
		
		if lst_s[i-1]=='+':
			if lst_s[i+1] not in '+-':
				lst_s.pop(i)
				lst_s.pop(index-1)
			else:
				lst_s.pop(i-1)
				lst_s.pop(i-1)
				lst_s.pop(index-2)			
		
		elif lst_s[i-1]=='-':
			new=[]
			new=map(minus,lst_s[i+1:index])
			lst_s[i+1:index]=new
			
			if lst_s[i+1] not in '+-':
				lst_s.pop(i)
				lst_s.pop(index-1)
			else:
				lst_s.pop(i-1)
				lst_s.pop(i-1)
				lst_s.pop(index-2)
		
		else:
			lst_s.pop(i)
			lst_s.pop(index-1)

	
	if lst_s[0]=='+':
		lst_s.pop(0)	
		
	return ''.join(lst_s)
				
def minus(chr):
	if chr=='+':
		res='-'
	elif chr=='-':
		res='+'
	else:
		res=chr
	return res
	
ex='(((((((((-((-(((n))))))))))))))'
print(solve(ex))


'''
Test.it("Basic tests")
Test.assert_equals(solve("a-(b)"),"a-b")
Test.assert_equals(solve("a-(-b)"),"a+b")
Test.assert_equals(solve("a+(b)"),"a+b")
Test.assert_equals(solve("a+(-b)"),"a-b")
Test.assert_equals(solve("(((((((((-((-(((n))))))))))))))"),"n")
Test.assert_equals(solve("(((a-((((-(-(f)))))))))"),"a-f")
Test.assert_equals(solve("((((-(-(-(-(m-g))))))))"),"m-g")
Test.assert_equals(solve("(((((((m-(-(((((t)))))))))))))"),"m+t")
Test.assert_equals(solve("-x"),"-x")
Test.assert_equals(solve("-(-(x))"),"x")
Test.assert_equals(solve("-((-x))"),"x")
Test.assert_equals(solve("-(-(-x))"),"-x")
Test.assert_equals(solve("-(-(x-y))"),"x-y")
Test.assert_equals(solve("-(x-y)"),"-x+y")
Test.assert_equals(solve("x-(y+z)"),"x-y-z")
Test.assert_equals(solve("x-(y-z)"),"x-y+z")
Test.assert_equals(solve("x-(-y-z)"),"x+y+z")
Test.assert_equals(solve("x-(-((-((((-((-(-(-y)))))))))))"),"x-y")
Test.assert_equals(solve("u-(v-w+(x+y))-z"),"u-v+w-x-y-z")
Test.assert_equals(solve("x-(s-(y-z))-(a+b)"),"x-s+y-z-a-b")
Test.assert_equals(solve("u+(g+v)+(r+t)"),"u+g+v+r+t")
Test.assert_equals(solve("q+(s-(x-o))-(t-(w-a))"),"q+s-x+o-t+w-a")
Test.assert_equals(solve("u-(v-w-(x+y))-z"),"u-v+w+x+y-z")
Test.assert_equals(solve("v-(l+s)-(t+y)-(c+f)+(b-(n-p))"),"v-l-s-t-y-c-f+b-n+p")
'''