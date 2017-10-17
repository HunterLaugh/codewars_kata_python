"""
Integers: Recreation One

Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays(in C an array of Pair), each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.

"""

# coding:utf-8
# m--n 之间数字，数字的因子平方和是某个数的平方和

def list_squared(m,n):
	square_number=[]
	
	for x in range(m,n+1):
		devisor=[]
		k=1
		while k*k<=x:
			if k*k==x:
				devisor.append(k)
			elif x%k==0:
				devisor.append(k)
				devisor.append(x//k)
			k+=1
	#		print("y",y)
	#	print("x",x,"y",y,"devisor",devisor)
			
		divisor_square=list(map(lambda x: x**2,devisor))
		sum_divisor_square=sum(divisor_square)
		
		if (int(sum_divisor_square **0.5))**2==sum_divisor_square:
			square_number.append([x,sum_divisor_square])
			
	return square_number
		
		
print(list_squared(1,250))		
#print(list_squared(42,250))
#print(list_squared(250,500))		