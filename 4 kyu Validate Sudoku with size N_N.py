'''
4 kyu  Validate Sudoku with size `NxN`

Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array(in Rust: Vec<Vec<u32>>) , ie:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Rules for validation

    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)


'''

# ---- row    ||| column   +++ palace

class Sudoku(object):
	def __init__(self,value):
		self.L=value
	
	def getN(self):
		return len(self.L)
	
	def get_listN(self):
		return list(range(1,N+1))		
	
	def is_N_N(self):
		for i in range(N):
			if len(self.L[i])!=n:
				return False

		return True


	def is_row(self):
		for each in self.L:
			each.sort()
			if each!=listN:
				return False
				
		return True		
	
	def is_column(self):
		j=0   # column
		while j<N:
			i=0   # row
			temp=[]
			while i<N:
				temp.append(self.L[i][j])
				i+=1
			temp.sort()
			if temp!=listN:
				return False
			j+=1
		
		return True
	
	
	def is_palace(self):
		pass


	N=self.getN()
	listN=self.get_listN()
	
	def is_valid(self):
		if self.is_N_N():
			if self.is_row():
				if self.is_column():
					return True
		
		return False		


testValue=[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

testSudoku=Sudoku(testValue)
print(testSudoku.is_valid())