'''
Path Finder #2 shortest path
Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the exit from the starting position. Otherwise, return false in JavaScript/Python and -1 in C++/C#/Java.

Empty positions are marked .. Walls are marked W. Start and exit positions are guaranteed to be empty in all test cases.
'''

import logging
logger=logging.getLogger()
logger.setLevel(30)

def path_finder(maze):
	sp=maze.split('\n')
	map=[]
	for i in sp:
		row=[]
		for j in i:
			row.append(j)
		map.append(row)

	dx=[1,0,-1,0]	# down right up left
	dy=[0,1,0,-1]
	
	start=[0,0]
	map[0][0]=1
	dest=[len(map)-1,len(map[0])-1]
	logging.debug(map)
	
	step=0
	foot=[[start]]
	while dest not in foot[-1]:
		next=[]
		for pre in foot[-1]:
			for idx in range(4):
				nextX=pre[0]+dx[idx]
				nextY=pre[1]+dy[idx]
				if nextX>=0 and nextX<len(map) and nextY>=0 and nextY<len(map[0]) and map[nextX][nextY]=='.' and ([nextX,nextY] not in next):
					next.append([nextX,nextY])
					map[nextX][nextY]=step+2
		step+=1	
		logging.debug(step)
		logging.debug(next)
		logging.debug(map)
		if not next:
			return False
		foot.append(next)

	logging.debug(map)
	logging.debug(step)
	return step		

# TEST CASE	---> PASSED ALL THE CASES
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

path_finder(a)		# epect  4
path_finder(b)		# epect  False
path_finder(c)		# epect  10
path_finder(d)		# epect  False
