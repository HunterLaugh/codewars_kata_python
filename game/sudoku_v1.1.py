# coding:utf-8
# 数独  9*9 二维数组，横行、竖列、3*3矩阵是1-2-3---9填充，不重复


import datetime 
class solution(object):
	def __init__(self,board):
		self.b=board	# 数独 9*9
		self.t=0		# 运行次数
	
	
	# 获得下一个未填的位置
	def get_next(self,x,y):
		# x row
		for col in range(y+1,9):
			if self.b[x][col]==0:
				return [x,col]
		# x+1 row-->9 row
		for row in range(x+1,9):
			for col in range(9):
				if self.b[row][col]==0:
					return [row,col]
		# 如果无0 --> -1
		return [-1,0]
	
	
	# 在row col matrix3*3 是否出现过
	def check(self,x,y,value):
		# row 行
		for col in range(9):
			if self.b[x][col]==value:
				return True
		# column 列
		for row in range(9):
			if self.b[row][y]==value:
				return True
		# matrix 3*3 宫
		row=x//3*3
		col=y//3*3
		row3col3=self.b[row][col:col+3]+self.b[row+1][col:col+3]+self.b[row+2][col:col+3]
		for r3c3_item in row3col3:
			if r3c3_item==value:
				return True
		return False
		
		
	# 回溯法
	def try_it(self,x,y):
		for i in range(1,10):
			self.t+=1
			if not self.check(x,y,i):
				self.b[x][y]=i
				next_x,next_y=self.get_next(x,y)
				if next_x==-1:		# 无有未填充项 结束
					return True
				else:
					end=self.try_it(next_x,next_y)
					if not end:		# end 为 None即无解
						self.b[x][y]=0
					else:
						return True

						
	def start(self):
		begin=datetime.datetime.now()
		if self.b[0][0]==0:
			self.try_it(0,0)
		else:
			x,y=self.get_next(0,0)
			self.try_it(x,y)		
		end=datetime.datetime.now()
		for i in range(9):
			print(self.b[i])
		print('cost %s time',end-begin)
		print('try times: ',self.t)

data=[[8,0,0,0,0,0,0,0,0],
	  [0,0,3,6,0,0,0,0,0],
	  [0,7,0,0,9,0,2,0,0],
	  [0,5,0,0,0,7,0,0,0],
	  [0,0,0,8,4,5,7,0,0],
	  [0,0,0,1,0,0,0,3,0],
	  [0,0,1,0,0,0,0,6,8],
	  [0,0,8,5,0,0,0,1,0],
	  [0,9,0,0,0,0,4,0,0]
	]		

s=solution(data)
s.start()