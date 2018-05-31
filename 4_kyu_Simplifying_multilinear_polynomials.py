# coding:utf-8
'''
Simplifying multilinear polynomials
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function:

simplify(poly)

that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

    All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:

    "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

    All monomials appears in order of increasing number of variables, e.g.:

    "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

    If two monomials have the same number of variables, they appears in lexicographic order, e.g.:

    "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

    There is no leading + sign if the first coefficient is positive, e.g.:

    "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

Good Work :)
'''
# 简化多项式，合并同类项，排序输出
# 输入：多项式
# 输出：多项式（合入同类项后，简化，排序后）
# 排序：1、按多项式len，即数量	2、按asccii码

# 解题思路：按'+-'分解poly，ascii码排序，并记录count alpha值
# 如poly '4abc+yz-3x-2zy‘分解为splitPoly ['4abc','yz','3x','-2yz']，并记countAlpha [3,2,1,2]
# 合并相同多因子
# 按len排序输出为string

# '-x-2xy' --> ['-x','-2xy']
def splitPoly(poly):
	# split poly with '+-' and sort()
	split=[]
	temp=[]
	for each in poly:
		if (each in '+-') and temp:
			temp.sort()
			split.append(''.join(temp))
			temp=[each]
		else:
			temp.append(each)
	
	temp.sort()
	split.append(''.join(temp))
	
	if split[0][0] not in '+-':
		split[0]='+'+split[0]

	return split

# '-2xy' --> '-'
def getOperator(string):
	if '-' in string:
		return '-'
	else:
		return '+'
		
# '-2xy' --> 2		
def getNum(string):
	num=[]
	for each in string:
		if each.isdigit():
			num.append(each)
	if not num:
		num=['1']
	return int(''.join(num))

# '-2xy' --> 'xy'	
def getPoly(string):
	res=[]
	for each in string:
		if each.isalpha():
			res.append(each)
	return ''.join(res)

	
def isSamePoly(str1,str2):
	return getPoly(str1)==getPoly(str2)
	
	
def addTwoStr(str1,str2):
	res=None
	if isSamePoly(str1,str2):
		op1=getOperator(str1)
		op2=getOperator(str2)
		num1=getNum(str1)
		num2=getNum(str2)
		if op1=='+' and op2=='+':
			num=num1+num2
		elif op1=='+' and op2=='-':
			num=num1-num2
		elif op1=='-' and op2=='+':
			num=-num1+num2
		else:
			num=-num1-num2
		
		if num>0:
			if num==1:
				res='+'+getPoly(str1)
			else:
				res='+'+str(num)+getPoly(str1)
		elif num==0:
			res=None
		else:
			if num==-1:
				res='-'+getPoly(str1)
			else:
				res=str(num)+getPoly(str1)
		
		return res


def addPoly(poly):
	i=0
	while i<len(poly)-1:
		j=i+1
		while j<len(poly):
			if isSamePoly(poly[i],poly[j]):
				poly[i]=addTwoStr(poly[i],poly[j])
				poly.pop(j)
				j-=1
				if not poly[i]:
					poly.pop(i)
					i-=1
					break
			j+=1
		i+=1
	return poly
	

# str1<str2 return True , else False 
def isMinToMax(str1,str2):
	s1=getPoly(str1)
	s2=getPoly(str2)
	if len(s1)<len(s2):
		return True
	elif len(s1)==len(s2):
		i=0
		while i<len(s1):
			if ord(s1[i])<ord(s2[i]):
				return True
			i+=1
	return False

	
def sortByLenAscii(poly):
	i=0
	while i<len(poly)-1:
		j=i+1
		while j<len(poly):
			if not isMinToMax(poly[i],poly[j]):
				temp=poly[i]
				poly[i]=poly[j]
				poly[j]=temp
			j+=1
		i+=1
			
	return poly
	
	
def simplify(poly):
	split=splitPoly(poly)
	print(split)
	add=addPoly(split)
	print(add)
	st=sortByLenAscii(add)
	print(st)
	if st[0][0]=='+':
		st[0]=st[0][1:]
	res=''.join(st)
	print(res)
	return ''.join(st)

		



# TEST CASE	PASSED ALL THE CASES IN CODEWAR
simplify("-x+2xy-y-xy-dc+dcba-c-dca-3xy-2abcd+2x")		#	 "cd+abcd"
'''
test.it("Test reduction by equivalence")


test.assert_equals(simplify("2xy-yx"),"xy")

test.assert_equals(simplify("-a+5ab+3a-c-2a"),"-c+5ab")

test.it("Test monomial length ordering")
test.assert_equals(simplify("-abc+3a+2ac"),"3a+2ac-abc")

test.assert_equals(simplify("xyz-xz"),"-xz+xyz")

test.it("Test lexicographic ordering")
test.assert_equals(simplify("a+ca-ab"),"a-ab+ac")

test.assert_equals(simplify("xzy+zby"),"byz+xyz")

test.it("Test no leading +")
test.assert_equals(simplify("-y+x"),"x-y")

test.assert_equals(simplify("y-x"),"-x+y")
'''