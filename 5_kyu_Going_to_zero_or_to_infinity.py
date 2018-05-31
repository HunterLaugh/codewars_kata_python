'''
5 kyu 
Going to zero or to infinity

Consider the following numbers (where n! is factorial(n)):

u1 = (1 / 1!) * (1!)

u2 = (1 / 2!) * (1! + 2!)

u3 = (1 / 3!) * (1! + 2! + 3!)

un = (1 / n!) * (1! + 2! + 3! + ... + n!)

Which will win: 1 / n! or (1! + 2! + 3! + ... + n!)?

Are these number going to 0 because of 1/n! or to infinity due to the sum of factorials?

#Task: Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n. Call this function "going(n)" where n is an integer greater or equal to 1.

To avoid discussions about rounding, if the result of the calculation is designed by "result", going(n) will return "result" truncated to 6 decimal places.

#Examples: 1.0000989217538616 will be truncated to 1.000098

1.2125000000000001 will be truncated to 1.2125

#Remark: Keep in mind that factorials grow rather rapidly, and you can need to handle large inputs.

'''

def going(n):
	L=[1]
	if n>1:
		for each in range(1,n):
			L.append(L[each-1]*(each+1))

	temp=(1/L[n-1])*(sum(L))

	# get six point number
	S=list(str(temp))
	count=0
	res=[]	
	for each in S:
		if count>=6:
			break
		if '.' not in res:
			res.append(each)
		else:
			res.append(each)
			count+=1
	
	# remove last zero
	for each in res[-1:-6]:
		if each!='0':
			break
		elif each=='.':
			break
		else:
			res.pop()
	
	result=float(''.join(res))
	
	return result
	


print(going(180))