'''
8 kyu
Calculate average 

Write function avg which calculates average of numbers in given list.
Python: Due to rounding issues please do not use statistics.mean or such.

'''

def find_average(array):
	n=len(array)
	if 0==n:
		return 0
	
	sum=0
	
	for each in array:
		sum=sum+each
		
	return sum/n
	
	