"""
Give me a Diamond
This kata is to practice simple string output. Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

###Task:

You need to return a string that displays a diamond shape on the screen using asterisk ("*") characters. Please see provided test cases for exact output format.

The shape that will be returned from print method resembles a diamond, where the number provided as input represents the number of *’s printed on the middle line. The line above and below will be centered and will have 2 less *’s than the middle line. This reduction by 2 *’s for each line continues until a line with a single * is printed at the top and bottom of the figure.

Return null if input is even number or negative (as it is not possible to print diamond with even number or negative number).

Please see provided test case(s) for examples.

Python Note

Since print is a reserved word in Python, Python students must implement the diamond(n) method instead, and return None for invalid input.

JS Note

JS students, like Python ones, must implement the diamond(n) method, and return null for invalid input.

"""

# coding:utf-8
# 格式化输出  钻石形状，使用 *　号
# 参数n 为最中间行的　*　数目，每行减２ 
# 偶数或负数　返回空


def diamond(n):
	if n%2==0 or n<0:
		return
	
	halfN=int((n-1)/2)
	
	iLine=1  # line
	jAsterisk=1	 # *
	kSpace=halfN	
	Result=""
	
	# 1--3--5--n
	while iLine<=halfN+1:		
		Result=Result+" " * kSpace
		Result=Result+"*" *jAsterisk + "\n"
		
		jAsterisk+=2
		kSpace-=1

		iLine+=1   
	
	jAsterisk=n-2
	kSpace=1
	
	# print n-2--n-4----1
	while iLine<=n:
		Result=Result+" " *kSpace
		Result=Result+"*" *jAsterisk+"\n"
		
		kSpace+=1
		jAsterisk-=2
		
		iLine+=1
	
	return Result	

	
print(diamond(5))

