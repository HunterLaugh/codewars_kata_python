# coding:utf-8
'''
Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
Examples

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
'''

# 判断数独是否正确解
# 数独：横行、竖列，宫，分别填入1-9数字，无重复

def validSolution(board):
# 分别判断：横行、竖列、宫，分别是否1-9无重复的数字
	# 横行
	i=0
	while i<9:
		if not isUnique(board[i][0:9]):
			return False
		else:
			i+=1
	
	# 竖列	
	for c in range(9):
		column=[]
		for r in range(9):
			column.append(board[r][c])
		if not isUnique(column):
			return False
				
	# 宫，9个宫  palace
	# 控制宫的移动,i -->往右移动，j 往下移动
	i=j=0  
	count=0
	while count<81:
		palace=[]		
		i=count%27//9
		j=count//27
		for r in range(0+3*j,3+3*j):
			for c in range(0+3*i,3+3*i):
				palace.append(board[r][c])
				count+=1
			
		if not isUnique(palace):
			return False

	return True

# 输入一个list，判断是否1--9	
def isUnique(L):	
	Unique=[1,2,3,4,5,6,7,8,9]
	L.sort()
	if L==Unique:
		return True
	else:
		return False

		
board=[
	[5, 3, 4, 6, 7, 8, 9, 1, 2], 
	[6, 7, 2, 1, 9, 0, 3, 4, 8],
	[1, 0, 0, 3, 4, 2, 5, 6, 0],
	[8, 5, 9, 7, 6, 1, 0, 2, 0],
	[4, 2, 6, 8, 5, 3, 7, 9, 1],
	[7, 1, 3, 9, 2, 4, 8, 5, 6],
	[9, 0, 1, 5, 3, 7, 2, 1, 4],
	[2, 8, 7, 4, 1, 9, 6, 3, 5],
	[3, 0, 0, 4, 8, 1, 1, 7, 9]
]		

testValue=[
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(validSolution(board))
print(validSolution(testValue))