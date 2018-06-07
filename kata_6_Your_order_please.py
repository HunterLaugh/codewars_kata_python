'''
Your order, please
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"

'''

import re
import logging

logger=logging.getLogger()
logger.setLevel(30)

def order(sentence):
	if not sentence:
		return ''
		
	num=[]
	split=sentence.split()
	for each in split:
		temp=re.search(r'(\d+)',each)
		num.append(int(temp.group()))
	
	i=0
	while i<len(num)-1:
		j=i+1
		while j<len(num):
			if num[i]>num[j]:
				tp=num[i]
				num[i]=num[j]
				num[j]=tp
				
				sp=split[i]
				split[i]=split[j]
				split[j]=sp
			j+=1
		i+=1
	
	logging.info('num: %s' % num)
	logging.info('split: %s' % split)
	
	return ' '.join(split)
	
# TEST CASE PASSED ALL  YOU CAN SEE IN THE TDD FOLDER
order("is2 Thi1s T4est 3a")