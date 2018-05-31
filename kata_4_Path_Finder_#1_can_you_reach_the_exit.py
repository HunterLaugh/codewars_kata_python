'''
Path Finder #1 can you reach the exit
Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
'''


def path_finder(MAZE):
	MAZE=MAZE.replace('\n',' ')
	MAZE=MAZE.split(' ')
	temp=[]
	maze=[]
	for each in MAZE:
		temp=list(each)
		maze.append(temp)
	
	n=len(maze)
	start=[0,0]
	destination=[n-1,n-1]
	route=[[0,0]]
	countStart=0
	x=0
	y=0
	while route[-1]!=[n-1,n-1]:
		if isValid(maze,x+1,y):
			route.append([x+1,y])
		elif isValid(maze,x,y+1):
			route.append([x,y+1])
		elif isValid(maze,x,y-1):
			route.append([x,y-1])
		elif isValid(maze,x-1,y):
			route.append([x-1,y])
		else:
			if route[-1]==[0,0]:
				countStart+=1
			else:
				route.pop()
		
		x=route[-1][0]
		y=route[-1][1]
		maze[x][y]=1
		if countStart>5:
			return False
		print(route)
	return True

def isValid(data,x,y):
	try:
		if x>=0 and x<len(data) and y>=0 and y<len(data) and data[x][y]=='.':
			return True
		else:
			return False
	except IndexError:
		return False
	
# TEST CASE
# PASS 504 : FAILED 2 ,CAN'T SEE THE FAIL INFO ,I CAN'T CHECK WHY. 
a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

e = "\n".join([
  "."
])

if path_finder(e):
	print('yes')
else:
	print('no')
