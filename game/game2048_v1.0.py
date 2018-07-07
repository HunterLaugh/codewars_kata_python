# coding:utf-8
'''
game 2048 

'''
import random
# map is 4*4 matrix ; score 
def initial():
	map=[]
	coordinate=[]
	for i in range(4):
		value=[]
		for j in range(4):
			value.append(0)
			coordinate.append([i,j])
		map.append(value)
	
	v1=random.choice([2,2,2,4,2])
	v2=random.choice([2,2,2,4,2])
	c1=random.randint(0,16-1)
	while 1:
		c2=random.randint(0,16-1)
		if c1!=c2:
			break
	r11,c11=coordinate[c1]
	r22,c22=coordinate[c2]
	map[r11][c11]=v1
	map[r22][c22]=v2
	return map
	
	
def display(map,score):
	if maxlist(map)>=2048:
		print('score %6d' % score[0])
		print('YOU WIN')
	else:
		print('score %6d' % score[0])
	print('********************************')
	for row in range(4):
		for column in range(4):
			if map[row][column]:
				print('%4d' %map[row][column],end=' ')
			else:
				print('    ',end=' ')				
		print()
	print('********************************')
	
	return 0

def clockwise90(map):
	n=4
	res=[]
	for i in range(4):
		row=[]
		for j in range(4):
			row.append(0)
		res.append(row)
		
	for row in range(4):
		for column in range(4):
			res[column][4-row-1]=map[row][column]
	
	for i in range(4):
		for j in range(4):
			map[i][j]=res[i][j]
	return map

def clockwise180(map):
	clockwise90(map)
	clockwise90(map)
	
def clockwise270(map):
	clockwise90(map)
	clockwise90(map)
	clockwise90(map)
	

def remove0(map):
	res=[]
	for i in range(4):
		temp=[]
		for j in range(len(map[i])):
			if map[i][j]:
				temp.append(map[i][j])
		res.append(temp)
	
	return res
	
		
def left(map,score):
	# remove 0 from map 
	mapN0=remove0(map)
	print(mapN0)
	# add same num in row 
	for i in range(len(mapN0)):
		for j in range(len(mapN0[i])-1):
			if mapN0[i][j]!=mapN0[i][j+1]:
				pass
			else:
				mapN0[i][j]=mapN0[i][j]*2
				score[0]+=mapN0[i][j]
				mapN0[i][j+1]=0
	print(mapN0)
	# remove 0 from mapN0
	newN0=remove0(mapN0)
	
	# add 0 , every row 4 num
	for i in range(4):
		for j in range(4):
			if j<len(newN0[i]):
				map[i][j]=newN0[i][j]
			else:
				map[i][j]=0
	return 1 
	

def right(map,score):
	clockwise180(map)
	left(map,score)
	clockwise180(map)
	return 1
	
	
def up(map,score):
	clockwise270(map)
	left(map,score)
	clockwise90(map)
	return 1
	

def down(map,score):
	clockwise90(map)
	left(map,score)
	clockwise270(map)
	return 1

	
def random2Or4(map):
	zeroCoord=[]
	for row in range(4):
		for column in range(4):
			if map[row][column]==0:
				zeroCoord.append([row,column])
	length=len(zeroCoord)
	if length==0:
		pass
	else:
		coordinate=random.randint(0,length-1)
		value=random.choice([2,2,2,4,2])
		r,c=zeroCoord[coordinate]
		map[r][c]=value
	return map
	
	
def isOver(map):
	# is zero space
	sum=0
	for i in range(4):
		sum+=map[i].count(0)
	if sum!=0:
		return False
	
	# is same between
	for r in range(4):
		for c in range(3):
			if map[r][c]==map[r][c+1]:
				return False
	for c in range(4):
		for r in range(3):
			if map[r][c]==map[r+1][c]:
				return False
	
	return True


def copylist(map):
	res=[]
	for i in range(len(map)):
		temp=[]
		for j in range(len(map[i])):
			temp.append(map[i][j])
		res.append(temp)
	return res


def maxlist(map):
	res=max(map[0])
	for i in range(1,4):
		if res<max(map[i]):
			res=max(map[i])
	return res
	
	
def start():
	score=[0]
	map=initial()
	display(map,score)
	while not isOver(map):
		pre=copylist(map)		
		
		operator=input('Your operator (a)left (w)up (s)down d(right):  ')
		if operator in 'aA':
			left(map,score)
		elif operator in 'wW':
			up(map,score)
		elif operator in 'sS':
			down(map,score)
		elif operator in 'dD':
			right(map,score)
		elif operator in 'qQ':
			print('Quit this game')
			return 0
		else:
			print('wrong enter, try again.')
			continue
		
		next=copylist(map)
		
		if not next==pre:
			random2Or4(map)
		display(map,score)
		
	if maxlist(map)>=2048:
		print('WINEER')
	else:
		print('LOSER')
		
	return 0
	
start()

data1=[
		[0,2,2,2],
		[0,2,2,2],
		[2,0,2,2],
		[0,2,0,2],
	]
#score1=[0]
#left(data1,score1)
#display(data1,score1)
#print(remove0(data1))