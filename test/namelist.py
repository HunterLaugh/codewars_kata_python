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
# 解题思路： 取出names list每个name加入到 listName中
# listName要转换为 string  ' Bart , Lisa & Maggie '

def namelist(names):
	nam=' '
	listName=[]
	n=len(names)
	if n==0:
		nam=' '
	elif n==1:
		nam=names[0].get('name')
	elif n>=2:
		# 取出key 'name' 对应的value
		for x in names:      
			listName.append(x.get('name'))
		# list转 str
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