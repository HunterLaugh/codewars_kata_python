"""
CamelCase Method

Write simple .camelcase method (camel_case function in PHP) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""
# coding:utf-8
# 首字母大写

def camel_case(string):
	st=string.split()
	li=[]
	
	for x in st:
		li.append(x.capitalize())
	
	re="".join(li)
	
	return re
	
print(camel_case("test case"))