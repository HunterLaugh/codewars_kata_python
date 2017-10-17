"""
Is a number prime?
Is Prime

Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
Assumptions

You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers.
Bug!
The Haskell version uses a wrong test case, where negative primes should also return True, e.g. it expects isPrime (-2) == True. Use abs or similar measures to take care of negative numbers. The test cases cannot get changed at this point. Sorry for the inconvenience.
"""

def is_prime(num):
	if type(num)==int:
		positiveNum=abs(num)
		if positiveNum in [0,1]:
			result=False
		elif positiveNum in [2,3]:
			result=True
		elif positiveNum%2==0:
			result=False
		else:
			result=True
			i=3
			while i<=positiveNum**0.5:
				if positiveNum%i==0:
					result=False
				i+=2
				
	return result
	
# test
print(is_prime(1))
print(is_prime(10))
print(is_prime(-21))
