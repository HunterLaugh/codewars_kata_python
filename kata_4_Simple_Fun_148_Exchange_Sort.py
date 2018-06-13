'''
Simple Fun #148 Exchange Sort
Task

Sorting is one of the most basic computational devices used in Computer Science.

Given a sequence (length ≤ 1000) of 3 different key values (7, 8, 9), your task is to find the minimum number of exchange operations necessary to make the sequence sorted.

One operation is the switching of 2 key values in the sequence.
Example

For sequence = [7, 7, 8, 8, 9, 9], the result should be0`.

It's already a sorted sequence.

For sequence = [9, 7, 8, 8, 9, 7], the result should be1`.

We can switching sequence[0] and sequence[5].

For sequence = [8, 8, 7, 9, 9, 9, 8, 9, 7], the result should be4`.

We can:

 [8, 8, 7, 9, 9, 9, 8, 9, 7] 
 switching sequence[0] and sequence[3]
 --> [9, 8, 7, 8, 9, 9, 8, 9, 7]
 switching sequence[0] and sequence[8]
 --> [7, 8, 7, 8, 9, 9, 8, 9, 9]
 switching sequence[1] and sequence[2]
 --> [7, 7, 8, 8, 9, 9, 8, 9, 9]
 switching sequence[5] and sequence[7]
 --> [7, 7, 8, 8, 8, 9, 9, 9, 9]

So 4 is the minimum number of operations for the sequence to become sorted.
Input/Output

    [input] integer array sequence

    The Sequence.

    [output] an integer

    the minimum number of operations.
'''
import logging

logger=logging.getLogger()
logger.setLevel(30)

def exchange_sort(sequence):
	logging.info('intial %s' % sequence)
	c7=sequence.count(7)
	c8=sequence.count(8)+c7
	c9=sequence.count(9)+c8
	
	expect=[]
	for i in range(c7):
		expect.append(7)
	for j in range(c7,c8):
		expect.append(8)
	for k in range(c8,c9):
		expect.append(9)
	logging.info('expect %s' % expect)
	
	time=0
	while sequence!=expect:
		# 8 <--> 7
		if (8 in sequence[:c7]) and (7 in sequence[c7:c8]):
			i8=sequence.index(8)
			i7=sequence[c7:c8].index(7)+c7
			sequence[i8]=7
			sequence[i7]=8
			time+=1
			logging.info('8<->7 %s' % sequence)
		# 9 <--> 8
		elif (9 in sequence[c7:c8]) and (8 in sequence[c8:]):
			i9=sequence[c7:c8].index(9)+c7
			i8=sequence[c8:].index(8)+c8
			sequence[i8]=9
			sequence[i9]=8
			time+=1
			logging.info('8<->7 %s' % sequence)
		# 9 <--> 7
		elif (9 in sequence[:c7]) and (7 in sequence[c8:]):
			i9=sequence.index(9)
			i7=sequence[c8:].index(7)+c8
			sequence[i9]=7
			sequence[i7]=9
			time+=1
			logging.info('9<->7 %s' % sequence)
		# 9 <--> 7
		elif (9 in sequence[:c7]) and (7 in sequence[c8:]):
			i9=sequence.index(9)
			i7=sequence[c8:].index(7)+c8
			sequence[i9]=7
			sequence[i7]=9
			time+=1
			logging.info('9<->7 %s' % sequence)		
		# 8,9 <--> 7 , 9 7 8 or 8 9 7
		else:
			i7=sequence[c7:].index(7)+c7
			if 8 in sequence[:c7]:
				i8=sequence.index(8)
				sequence[i8]=7
				sequence[i7]=8
			else:
				i9=sequence.index(9)
				sequence[i9]=7
				sequence[i7]=9
			time+=1
			logging.info('89<->7 %s' % sequence)				
	return time 

			
			
# TEST CASE	 PASSED ALL THE CASES
s1=[9, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7]
exchange_sort(s1)




