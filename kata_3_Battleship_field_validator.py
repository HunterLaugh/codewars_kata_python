# coding:utf-8
'''
Battleship field validator
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:

    There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.

    Each ship must be a straight line, except for submarines, which are just single cell.

    The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link.

'''
# input 10*10 list ---> output: True or False
# 1、为1条直线，横或竖
# 2、数量与长度限制 battle 1*4--cruiser 2*3--destroy 3*2--submarines 4*1
# 3、舰之间不能接触，边与角都不能接触
# ps: 10*10 二维数组

# point in 10*10 grid 
def validCoord(point):
	x,y=point
	if x>=0 and x<10 and y>=0 and y<10:
		return True
	else:
		return False

		
# point: edge and corner		
def around(point):
	x,y=point
	res=[]
	ar=[[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
	for each in ar:
		if validCoord(each):
			res.append(each)
	return res


def validateBattlefield(field):
	N=10
	# get coordinate
	coordinate=[]
	for x in range(N):
		for y in range(N):
			if field[x][y]==1:
				coordinate.append([x,y])

	# 1*4+2*3+3*2+4*1=20
	if 20!=len(coordinate):
		return False
		
	# copy coordinate
	cpCoord=[]
	for each in coordinate:
		cpCoord.append(each)
		
	# battleship 1*4
	battleship=[]
	for x in range(N):
		for y in range(N):
			if ([x,y] in coordinate) and ([x,y+1] in coordinate) and ([x,y+2] in coordinate) and ([x,y+3] in coordinate):
				battleship=[[x,y],[x,y+1],[x,y+2],[x,y+3]]
				break
		if battleship:
			break
	if not battleship:
		for y in range(N):
			for x in range(N):
				if ([x,y] in coordinate) and ([x+1,y] in coordinate) and ([x+2,y] in coordinate) and ([x+3,y] in coordinate):
					battleship=[[x,y],[x+1,y],[x+2,y],[x+3,y]]
					break
			if battleship:
				break
	if not battleship:
		return False
	# battleship 1*4	not contact		
	for each in battleship:
		arnd=around(each)
		for item in arnd:
			if (item not in battleship) and (item in cpCoord):
				return False	
	
	for each in battleship:
		coordinate.remove(each)
		
	# cruisers 2*3
	cruisers=[]
	count=0
	for x in range(N):
		for y in range(N):
			if ([x,y] in coordinate) and ([x,y+1] in coordinate) and ([x,y+2] in coordinate) :
				cruisers.append([[x,y],[x,y+1],[x,y+2]])
				count+=1
			if count==2:
				break
		if count==2:
			break
	if count!=2:
		for y in range(N):
			for x in range(N):
				if ([x,y] in coordinate) and ([x+1,y] in coordinate) and ([x+2,y] in coordinate) :
					cruisers.append([[x,y],[x+1,y],[x+2,y]])
					count+=1
				if count==2:
					break
			if count==2:
				break
	if count!=2:
		return False
	# cruisers 2*3	-- not contact
	for each in cruisers:
		for ev in each:
			arnd=around(ev)
			for item in arnd:
				if (item not in each) and (item in cpCoord):
					return False
	
	for each in cruisers:
		for ev in each :
			coordinate.remove(ev)

	# destroyers 3*2
	destroyers=[]
	count=0
	for x in range(N):
		for y in range(N):
			if ([x,y] in coordinate) and ([x,y+1] in coordinate):
				destroyers.append([[x,y],[x,y+1]])
				count+=1
			if count==3:
				break
		if count==3:
			break
	if count!=3:
		for y in range(N):
			for x in range(N):
				if ([x,y] in coordinate) and ([x+1,y] in coordinate) :
					destroyers.append([[x,y],[x+1,y]])
					count+=1
				if count==3:
					break
			if count==3:
				break
	if count!=3:
		return False	
	# destroyers 3*2	-- not contact
	for each in destroyers:
		for ev in each:
			arnd=around(ev)
			for item in arnd:
				if (item not in each) and (item in cpCoord):
					return False
					
	for each in destroyers:
		for ev in each :
			coordinate.remove(ev)

	# submarines 4*1	
	submarines=[]
	for each in coordinate:
		submarines.append(each)
	if len(submarines)!=4:
		return False

	# submarines 4*1	-- not contact
	for each in submarines:
		arnd=around(each)
		for item in arnd:
			if item in cpCoord:
				return False
				
	return True
	


# TEST CASE		---> PASSED ALL THE CASES
battleField = 	[[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

if validateBattlefield(battleField):		# True	
	print('Yes')
else:
	print('No')
	




