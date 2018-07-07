# coding:utf-8
# game 2048  New
'''
initial-->display-->
move:left,right,up,down-->random2or4-->
isOver
'''
import random

# 常量定义 ，SCORE 得分，MAX 最大数值
SCORE=0
DATA=[2,2,4,2,2]
MAP2=[[1,2,3,4],
	 [5,6,7,8],
	 [0,2,2,2],
	 [0,4,4,0]
	]
MAP=[[0,0,0,0],
	 [0,0,0,0],
	 [0,0,0,0],
	 [0,0,0,0]
	]
	
COORDINATE=[[0,0],[0,1],[0,2],[0,3],
			[1,0],[1,1],[1,2],[1,3],
			[2,0],[2,1],[2,2],[2,3],
			[3,0],[3,1],[3,2],[3,3]
			]

			
# 初始化4*4二维矩阵，随机2个数（2,4)
def initial():
	i1=random.randint(0,15)
	while 1:
		i2=random.randint(0,15)		
		if i1!=i2:
			break
	v1=random.choice(DATA)
	v2=random.choice(DATA)
	r1,c1=COORDINATE[i1]
	r2,c2=COORDINATE[i2]	
	MAP[r1][c1]=v1
	MAP[r2][c2]=v2
	
def display():
	if maxlist()>2048:
		print('WINNER, SCORE %6d' % SCORE)	
	else:
		print('COME ON, SCORE %6d' % SCORE)
	print('################################')
	for i in range(4):
		for j in range(4):
			if MAP[i][j]:
				print('%6d' % MAP[i][j],end='')
			else:
				print('      ' ,end='')
		print()
	print('################################')

	
def copyMap():
	res=[]
	for i in range(4):
		temp=[]
		for j in range(4):
			temp.append(MAP[i][j])
		res.append(temp)
	return res 
		
	
# 顺时针旋转90度	
def clockwise90():
	new=[]
	for i in range(4):
		temp=[]
		for j in range(4):
			temp.append(MAP[i][j])
		new.append(temp)
		
	for i in range(4):
		for j in range(4):
			MAP[j][4-i-1]=new[i][j]
	
def clockwise180():
	clockwise90()
	clockwise90()	
	
def clockwise270():
	clockwise90()
	clockwise90()
	clockwise90()


# move left，same num add ，结果往左靠
def left():
	global SCORE
	# row [2,0,4,0] remove 0 -->[2,4]
	rm_zero=[]
	for i in range(4):
		temp=[]
		for j in range(4):
			if MAP[i][j]:
				temp.append(MAP[i][j])
		rm_zero.append(temp)
		
	# add same row [2,2,4]-->[4,4]
	for i in range(4):
		j=0
		while j<len(rm_zero[i])-1:
			if rm_zero[i][j]==rm_zero[i][j+1]:
				rm_zero[i][j]=rm_zero[i][j]*2
				SCORE+=rm_zero[i][j]
				rm_zero[i].pop(j+1)
			j+=1
					
	for i in range(4):
		for j in range(4):
			if j<len(rm_zero[i]):
				MAP[i][j]=rm_zero[i][j]
			else:
				MAP[i][j]=0
	
	
def right():
	clockwise180()
	left()
	clockwise180()
	
def up():
	clockwise270()
	left()
	clockwise90()
	
def down():
	clockwise90()
	left()
	clockwise270()
	

# over -> True , not False
def isOver():
	# MAP  have 0 or not 
	for i in range(4):
		for j in range(4):
			if MAP[i][j]==0:
				return False
	
	# in row have same num between 
	for i in range(4):
		for j in range(4-1):
			if MAP[i]==MAP[i][j+1]:
				return False
				
	# in column have same num between 
	for j in range(4):
		for j in range(4-1):
			if MAP[i][j]==MAP[i+1][j]:
				return False
				
	return True 


def maxlist():
	res=max(MAP[0])
	for i in range(1,4):
		if res<max(MAP[i]):
			res=max(MAP[i])
	return res		
	
	
def random2or4():
	zero=[]
	for i in range(4):
		for j in range(4):
			if MAP[i][j]==0:
				zero.append([i,j])
	r,c=random.choice(zero)
	value=random.choice(DATA)
	MAP[r][c]=value
	
def play():
	initial()
	display()
	while not isOver():
		op=input('operator: a(left) d(right) w(up) s(down): ')
		pre=copyMap()
		if op in 'aA':
			left()
		elif op in 'dD':
			right()
		elif op in 'wW':
			up()
		elif op in 'sS':
			down()
		elif op in 'qQ':
			if maxlist()>=2048:
				print('WINNER !!!')
			print('Quit this game!')
			break
		else:
			continue
		next=copyMap()
		if pre==next:
			continue
		random2or4()
		display()
	
play()


	