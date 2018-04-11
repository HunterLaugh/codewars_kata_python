# coding:utf-8
'''
用0,1组成二维数组表示迷宫maze，1表示可以通行，0表示墙，求从入口到出口的路径

'''

maze=[
	[1,1,0,1,1,0,1],
	[0,1,1,1,0,0,0],
	[1,0,1,0,1,1,1],
	[0,1,1,0,1,0,1],
	[0,1,1,1,1,0,1],
	[1,1,0,1,0,1,1],
	[0,0,1,1,0,0,1]]

# 迷宫入口
start_location=(0,0)
# 迷宫出口
destination=(6,6)
# 走过的路
trace=[(0,0)]

# 有效的路 	1可走  0不可走
def valid(maze,x,y):
	print(maze[x,y],x,y)
	if x>=0 and x<len(maze) and y>=0 and y<len(maze[0] and maze[x,y]==1:
		return True
	return False

	
def move(maze,x,y):
	if trace[-1]==(6,6):
		print('Successful !')
		print(trace)
		return True 
			
	if valid(maze,x,y):
		trace.append((x,y))
		maze[x,y]=2
	
	if not move(maze,x-1,y):
		
	
		

move(maze,0,0)