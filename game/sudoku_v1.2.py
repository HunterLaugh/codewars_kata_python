# coding:utf-8
# 数独  9*9 二维数组，横行、竖列、3*3矩阵是1-2-3---9填充，不重复


import datetime 
class solution(object):
	def __init__(self,board):
		self.b=board	#数独--待解
		self.t=0		#计算次数
		self.space=[]	#需填充的空格
		self.route=[]

		
	# 行 列 小九宫格 是否有重复的值	
	def check(self,x,y,value):
		# 行
		for col in range(9):
			if self.b[x][col]==0:
				return True
		# 列
		for row in range(9):
			if self.b[row][y]==0:
				return True
		# 小九宫格
		x=x//3*3
		y=y//3*3
		for i in range(x,x+3):
			for j in range(y,y+3):
				if self.b[i][j]==0:
					return True
		return False

	
	# 需填充的空格
	def get_space(self):
		for i in range(9):
			for j in range(9):
				if self.b[i][j]==0:
					self.space.append((i,j))
		return True
		
		
	# 可以填充的值
	def valid(self):
		idx=0
		for x,y in self.space:
			temp=[]
			for v in range(1,10):
				if not check(x,y,v):
					temp.append(v)	
			self.space[idx].append(temp)
			idx+=1
		return True
		
			
	# 排序，len(可选值)-->小在前，排序n之后的
	def sort_len(self):
		n=len(self.space)
		for i in range(n-1):
			for j in range(i+1,n):
				if len(self.space[i][1])>len(self.space[j][1]):
					temp=self.space[i]
					self.space[i]=self.space[j]
					self.space[j]=temp
		return True
		

	def play(self):
		i=0
		for i range(flag,len(self.space)):
			(x,y)=self.space[i][0]
			value=self.space[i][1]
			flag=0
			j=0
			while j<len(value):
				if check(x,y,value[j]):	#重复，尝试下一个
					j+=1
					flag+=1
					continue
				else:
					self.space[i].append(flag)
					self.route.append(self.space[i])
					break
		
		
		
		
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