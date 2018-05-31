'''
Date Format Validation
Create a function that will return true if the input is in the following date time format 01-09-2016 01:20 and false if it is not.

This Kata has been inspired by the Regular Expressions chapter from the book Eloquent JavaScript.

'''

import re
def date_checker(date):
	res=re.search(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}',date)
	if res:
		return True
	else:
		return False
	
# TEST CASE  PASSED ALL
a='01-09-2016 01:20'    # True
b='01-09-2016 01;20'    # False
date_checker(a)
date_checker(b)