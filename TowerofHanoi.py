# coding:utf-8
# 汉诺塔 TowerofHanoi

# 3根柱子  start  temp  dest ，圆盘 n个
# PASSED ALL CASE

def move(pan,start,destination):
	print(pan,start,'>>>',destination)
	
def hanoi(n,start='start',temp='temp',dest='dest'):
	print('n',n)
	print('start',start,'temp',temp,'dest',dest)

	if n==1:
		move(1,start,dest)
	else:
		hanoi(n-1,start,dest,temp)
		move(n,start,dest)
		hanoi(n-1,temp,start,dest)

hanoi(2)