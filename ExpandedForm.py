"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
"""

# coding:utf-8
# 结果   123-->100+20+3  ;  100200-->100000+200
# 如123  int 转成 str  ；str 转 list； list转成 1*10次方，2*10次方,3*10次方 list；  list转成 string
# 注意  中间有0，末尾有0

def expanded_form(num):
	st=str(num)
#	print(st)
	li=list(st)
#	print(li)
	n=len(li)
	tempLi=[]
	i=0
	for x in li:
		tempLi.append(int(x)*(10**(n-1-i)))
#		print(tempLi)
		i+=1
	
	strLi=str(tempLi[0])
	for x in tempLi[1:n]:
		if x!=0:
			strLi=strLi+' + '+str(x)
	
	return strLi

print(expanded_form(123))
print(expanded_form(10203))
print(expanded_form(1020300))