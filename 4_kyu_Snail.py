'''
Snail
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
NOTE 2: The 0x0 (empty matrix) is represented as [[]]

'''

# coding:utf-8
# 顺时针取二维数组的值，设index(x,y)  分别为  y+1 >> x+1 >> y-1 >> x-1
def snail(array):
	N=len(array)
	res=[]
	x=0
	y=0
	time=0
	try:
		while 1:
			for y in range(time,N-time):
				res.append(array[x][y])
				if len(res)==N*N:
					return res
			y=N-time-1
		
			for x in range(time+1,N-time):
				res.append(array[x][y])
				if len(res)==N*N:
					return res
			x=N-time-1
			
			for y in range(N-time-2,time-1,-1):
				res.append(array[x][y])
				if len(res)==N*N:
					return res
			y=time
			
			for x in range(N-time-2,time,-1):
				res.append(array[x][y])
				if len(res)==N*N:
					return res
			x=time+1
			
			time+=1
	except IndexError:
		print('time',time)
		print('x',x,'y',y)
		return res
	
# TEST CASE  PASSED ALL 
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]


b=[[ 1,  2,  3,  4,  5],
   [ 6,  7,  8,  9, 10],
   [11, 12, 13, 14, 15],
   [16, 17, 18, 19, 20],
   [21, 22, 23, 24, 25]]
# expect  [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
	 
print(snail(a))
print(snail(b))