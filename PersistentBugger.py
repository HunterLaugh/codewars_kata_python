"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""

def persistence(n):
	count=0
	while n>=10:
		if n>=100000 :
			single=n%10
			tens=n%100//10
			hundreds=n%1000//100
			thousands=n%10000//1000
			millions=n%100000//10000
			tenMillion=n//100000
			n=single*tens*hundreds*thousands*millions*tenMillion
			count=count+1            
		elif n>=10000:
			single=n%10
			tens=n%100//10
			hundreds=n%1000//100
			thousands=n%10000//1000
			millions=n//10000
			n=single*tens*hundreds*thousands*millions
			count=count+1
		elif n>=1000 :
			single=n%10
			tens=n%100//10
			hundreds=n%1000//100
			thousands=n//1000
			n=single*tens*hundreds*thousands
			count=count+1
		elif n>=100:
			single=n%10
			tens=n%100//10
			hundreds=n//100
			n=single*tens*hundreds
			count=count+1
		elif n>=10:
			single=n%10
			tens=n//10
			n=single*tens
			count=count+1
	
	return count
		
print("persistence(39)",persistence(39))
print("persistence(4)",persistence(4))
print("persistence(25)",persistence(25))
print("persistence(999)",persistence(999))
print("persistence(8174)",persistence(8174))
print("persistence(-21)",persistence(-21))			