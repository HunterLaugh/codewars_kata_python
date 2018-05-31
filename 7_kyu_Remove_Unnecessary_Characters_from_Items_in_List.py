'''
Remove Unnecessary Characters from Items in List
You've been given a list that states the daily revenue for each day of the week. Unfortunately, the list has been corrupted and contains extraneous characters. Rather than fix the source of the problem, your boss has asked you to create a program that removes any unneccessary characters and return the corrected list.

The expected characters are digits, ' $ ', and ' . ' All items in the returned list are expected to be strings.

For example:

a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
remove_char(a1) 
>>> ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']

corrupted2 = ['%%$...9p2. 42', '"e"$15o.4/d9', '$29.29', ',$,5$$$9,.,25', 'E$5.0O0']
>>> fixed2 = ['$92.42', '$15.49', '$29.29', '$59.25', '$5.00']

corrupted1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
>>> fixed1 = ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']

'''

import re
def remove_char(array):
	new=[]
	for each in array:
		temp=re.sub(r'\D','',each)
		a=list(temp)
		a.insert(0,'$')
		a.insert(-2,'.')
		b=''.join(a)
		new.append(b)
		
	return new
	
		
# TEST CASE	PASSED ALL
corrupted1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']

corrupted2 = ['%%$...9p2. 42', '"e"$15o.4/d9', '$29.29', ',$,5$$$9,.,25', 'E$5.0O0']

corrupted3 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']

print(remove_char(corrupted1))
