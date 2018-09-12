# coding:utf-8
# 4位数的+运算，或2位数的乘运算

import random

def add_():
	print()
	print('=================================')
	while 1:
		x=random.randint(1000,9999)
		y=random.randint(1000,9999)
		print('%s+%s' %(x,y))
		res=input('=')
		if res in 'qQ':
			break
		elif res.isdigit()==True and int(res)==x+y:
			print('RINGT ANSWER')
		else:
			print('WRONG, RINGT ANSWER IS: %s' %(x+y))
		print('=================================')

	return 0
	
	
def multiply_():
	print()
	print('=================================')
	while 1:
		x=random.randint(10,99)
		y=random.randint(10,99)
		print('%s*%s' %(x,y))
		res=input('=')
		if res in 'qQ':
			break
		elif res.isdigit()==True and int(res)==x*y:
			print('RINGT ANSWER')
		else:
			print('WRONG, RINGT ANSWER IS: %s' %(x*y))
		print('=================================')

	return 0
	
	

def start():
	while 1:
		print('select\n (1) add: 4th add 4th\n (2) multiply: 2th multiply 2th\n (q or Q) quit')
		operater=input('Your select: ')
		if operater=='1':
			add_()
		elif operater=='2':
			multiply_()
		elif operater in 'qQ':
			break
		else:
			continue
	
	return 0
	
	
start()
