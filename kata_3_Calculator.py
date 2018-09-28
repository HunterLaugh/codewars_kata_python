'''
Calculator
Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.

'''
class Calculator(object):
	def __init__(self):
		pass
		
	def evaluate(self, string):
		# verify string is valid
		L=string.split(' ')
		i=0
		for each in L:
			if '.' in each:
				L[i]=float(each)
			elif each.isdigit():
				L[i]=int(each)
			else:
				pass
			i+=1
		print(L)
		while len(L)>2:
			mult,div,add,minus=[999,999,999,999]
			try:
				mult=L.index('*')
			except:
				pass
			try:
				div=L.index('/')
			except:
				pass			
			if mult<div:
				idx=mult
				temp=L[idx-1]*L[idx+1]
			elif mult>div:
				idx=div
				temp=L[idx-1]//L[idx+1]
			else:
				try:
					add=L.index('+')
				except:
					pass
				try:
					minus=L.index('-')
				except:
					pass
				if add<minus:
					idx=add
					temp=L[idx-1]+L[idx+1]
				else :
					idx=minus
					temp=L[idx-1]-L[idx+1]
			L[idx-1]=temp
			L.pop(idx)
			L.pop(idx)
		print(L[0])
		return L[0]		
			
		
		
# TEST CASE	--> PASSED ALL THE CASES
t1="2 / 2 + 3 * 4 - 6"
t2="1.1 + 2.2 * 3.3"
cal=Calculator()
cal.evaluate(t1)
cal.evaluate(t2)
		
