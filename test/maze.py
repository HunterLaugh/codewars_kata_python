# coding:utf-8
# 迷宫

# 1可走  0不可走
data=[
	[1,1,0,1,1,0,1],
	[0,1,1,1,0,0,0],
	[1,0,1,0,1,1,1],
	[0,1,1,0,1,0,1],
	[0,1,1,1,1,0,1],
	[1,1,0,1,0,1,1],
	[0,0,1,1,0,0,1]]

for each in range(7):
	print(data[each])
	
trace=[[0,0]]

# 判断是否可走 1 yes  0 no
def valid(data,x,y):
	if x>=0 and x<len(data) and y>=0 and y<len(data[0]) and data[x][y]==1:
		return True 
	else:
		return False

x=0
y=0
count=0
while trace[-1]!=[6,6] and count<40:	
	# move right
	if valid(data,x,y+1):
		trace.append([x,y+1])
	
	# move down
	elif valid(data,x+1,y):
		trace.append([x+1,y])		

	# move up
	elif valid(data,x-1,y):
		trace.append([x-1,y])
	
	# move left
	elif valid(data,x,y-1):
		trace.append([x,y-1])
	
	# 无效，返回
	else:
		trace.pop()
	
	x=trace[-1][0]
	y=trace[-1][1]
	data[x][y]=2
	count+=1

print('\n\nsuccessfull')	


for each in range(7):
	print(data[each])

print('\n\n',trace)

		
		