"""
WeIrD StRiNg CaSe
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

for example:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""

# coding:utf-8
# 解题思路
# 字符串分拆为单个字符串 s.plit()-->字符串转换为 list-->判断list 字符大小写情况 if i%2==0 : L[i].upper()     if i%2==1: L[i].lower()-->list合成string

# s.islower() 所有字符都是小写
# s.isupper() 所有字符都是大写
# s.upper()  把所有字符大写
# s.lower()  把所有字符小写

# string 无法被修改  string[i]=string[i].upper()  错误的，string[i]无法被重新赋值

def to_weird_case(string):
	# your code
	n=len(string)
	i=0
	j=0
	
	Li=list(string)
	
	while i<n :
#		print("start",i,string[i])
		if string[i]==" ":
			j=0
		elif j%2==0: # and string[j].islower():
			Li[i]=string[i].upper()
			j+=1
#			print("0 2 ")
		elif j%2==1: # and string[i].isupper():
			Li[i]=string[i].lower()
			j+=1
#			print("1 3")
#		print("end",i,Li[i])

		i+=1
	
	Result=""
	for x in Li:
		Result=Result+x
	
			
	return Result

print(to_weird_case("This"))
print(to_weird_case("ihIs"))