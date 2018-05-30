'''
Escape the maze
That's terrible! Some evil korrigans have abducted you during your sleep and threw you into a maze of thorns in the scrubland D:
But have no worry, as long as you're asleep your mind is floating freely in the sky above your body.

    Seeing the whole maze from above in your sleep, can you remember the list of movements you'll have to do to get out when you awake?

Input

You are given the whole maze as a 2D grid (an array of strings) with the following specifications:

    ' ' is some walkable space
    '#' is a thorn bush
    '^', '<', 'v' or '>' is your sleeping body facing respectively the top, left, bottom or right side of the map.

Output

Write the function escape that return the list of movements you need to do relatively to the direction you're facing in order to escape the maze (you won't be able to see the map when you wake up). as an array of the following instructions:

    'F' move one step forward
    'L' turn left
    'R' turn right
    'B' turn back

        Note: 'L','R', and 'B' ONLY perform a rotation and will not move your body

If the maze has no exit, return an empty array.

    This is a real maze, there is no "escape" point. Just reach the edge of the map and you're free!
    You don't explicitely HAVE to find the shortest possible route, but you're quite likely to timeout if you don't ;P
    Aside from having no escape route the mazes will all be valid (they all contain one and only one "body" character and no other characters than the body, "#" and " ". Besides, the map will always be rectangular, you don't have to check that either)

'''
def getDirectLocation(maze):		
	i=0
	while i<len(maze):
		j=0
		while j<len(maze[i]):
			if maze[i][j] in ['^','<','v','>']:
				direct=maze[i][j]
				location=[i,j]
				return [direct,location]
			j+=1
		i+=1

		
def isExit(maze,location):
	row=len(maze)
	column=len(maze[0])
	if (location[0] in [0,row-1]) or (location[1] in [0,column-1]):
		return True
	else:
		return False


def valid(maze,location):
	i=location[0]
	j=location[1]
	if maze[i][j]==' ':
		return True
	else:
		return False		

		
def getRoadmap(maze):
	roadmap=[]
	DL=getDirectLocation(maze)
	direct=DL[0]
	roadmap.append(DL[1])
	
	maze_list=[]
	for each in maze:
		maze_list.append(list(each))
	
	row=roadmap[-1][0]
	column=roadmap[-1][1]	
	while not isExit(maze,roadmap[-1]):
		# try: down		right	left	up	  
		if valid(maze_list,[row+1,column]):
			roadmap.append([row+1,column])
		elif valid(maze_list,[row,column+1]):
			roadmap.append([row,column+1])
		elif valid(maze_list,[row,column-1]):
			roadmap.append([row,column-1])
		elif valid(maze_list,[row-1,column]):
			roadmap.append([row-1,column])			
		else:
			roadmap.pop()
			if not roadmap:
				print('no way this maze')
				print(maze)
				return []
		row=roadmap[-1][0]
		column=roadmap[-1][1]
		if maze_list[row][column]!=direct:
			maze_list[row][column]=1
	return roadmap


def dataChangeOfDirect(d1,d2):
	d=''.join([d1,d2])
	if d in ['UR','RD','DL','LU']:
		res=['R','F']
	elif d in ['UU','RR','DD','LL']:
		res=['F']
	elif d in ['UD','DU','LR','RL']:
		res=['B','F']
	else:
		res=['L','F']
	return res
		
def exchange(direct,roadmap):
	if not roadmap:
		return []
	
	minus=[]
	i=1
	while i<len(roadmap):
		rowMinus=roadmap[i][0]-roadmap[i-1][0]
		columnMinus=roadmap[i][1]-roadmap[i-1][1]
		minus.append([rowMinus,columnMinus])
		i+=1
	
	direction=[]
	da1={'^':'U','<':'L','v':'D','>':'R'}
	direction.append(da1[direct])
		
	for each in minus:
		if each==[0,1]:
			direction.append('R')
		elif each==[0,-1]:
			direction.append('L')
		elif each==[1,0]:
			direction.append('D')
		elif each==[-1,0]:
			direction.append('U')
		else:
			print('ERROR')
	
	res=[]
	index=0
	while index<len(direction)-1:
		newDirect=dataChangeOfDirect(direction[index],direction[index+1])
		for each in newDirect:
			res.append(each)
		index+=1
	
	return res
	
		
def escape(maze):
	print(maze)
	direct=getDirectLocation(maze)[0]
	print(direct)
	roadmap=getRoadmap(maze)
	print(roadmap)
	print()
	res=exchange(direct,roadmap)
	print(res)
	return res
	
# TEST CASE		PASSED ALL THE CASES
a=[
  '# #',
  ' > ',
  '# #'
]

b=[
  '###########',
  '#>        #',
  '######### #'
]

c=[
  "#########################################",
  "#<    #       #     #         # #   #   #",
  "##### # ##### # ### # # ##### # # # ### #",
  "# #   #   #   #   #   # #     #   #   # #",
  "# # # ### # ########### # ####### # # # #",
  "#   #   # # #       #   # #   #   # #   #",
  "####### # # # ##### # ### # # # #########",
  "#   #     # #     # #   #   # # #       #",
  "# # ####### ### ### ##### ### # ####### #",
  "# #             #   #     #   #   #   # #",
  "# ############### ### ##### ##### # # # #",
  "#               #     #   #   #   # #   #",
  "##### ####### # ######### # # # ### #####",
  "#   # #   #   # #         # # # #       #",
  "# # # # # # ### # # ####### # # ### ### #",
  "# # #   # # #     #   #     # #     #   #",
  "# # ##### # # ####### # ##### ####### # #",
  "# #     # # # #   # # #     # #       # #",
  "# ##### ### # ### # # ##### # # ### ### #",
  "#     #     #     #   #     #   #   #    ",
  "#########################################"
]

escape(b)
mazes=[]
mazes.append(a)
mazes.append(b)
mazes.append(c)
for maze in mazes:
	escape(maze)
	pass