# coding:utf-8
"""
Format a string of names like 'Bart, Lisa & Maggie'.

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""
# ����˼·�� ȡ��names listÿ��name���뵽 listName��
# listNameҪת��Ϊ string  ' Bart , Lisa & Maggie '

def namelist(names):
	nam=' '
	listName=[]
	n=len(names)
	if n==0:
		nam=' '
	elif n==1:
		nam=names[0].get('name')
	elif n>=2:
		# ȡ��key 'name' ��Ӧ��value
		for x in names:      
			listName.append(x.get('name'))
		# listת str
		index=0
		for y in  listName:
			if index==(n-2):
				nam=y.get('name')+'&'+y
			else:
				nam=nam+','+y
			index=index+1
	
	return nam

	
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'} ]))