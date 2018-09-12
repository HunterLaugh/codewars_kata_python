'''
Shortest Knight Path
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)

'''
import logging
logger=logging.getLogger()
logger.setLevel(10)

# 'a1' --> [7][0]
def exchange(pos):
	column_base=['a','b','c','d','e','f','g','h']
	column=column_base.index(pos[0])
	row=8-int(pos[1])
	return [row,column]

def isInner(position):
	if position[0]>=0 and position[0]<8 and position[1]>=0 and position[1]<8:
		return True
	else:
		return False

def valid(start,board):
	row=start[0]
	column=start[1]
	base=[[row-2,column-1],[row-2,column+1],[row-1,column+2],[row+1,column+2],[row+2,column+1],[row+2,column-1],[row+1,column-2],[row-1,column-2]]
	res=[]
	for each in base:
		if isInner(each) and board[each[0]][each[1]]==0:
			res.append(each)
	return res 

def knight(p1, p2):
	board=[]
	for i in range(8):
		row=[]
		for j in range(8):
			row.append(0)
		board.append(row)
		
	start=exchange(p1)
	end=exchange(p2)
	logging.info(board)
	
	foot=[start]
	time=1
	while end not in foot[-1]:
		next=[]
		if foot[-1]==start:
			next=valid(start,board)
			for each in next:
				board[each[0]][each[1]]=time
		else:
			for each in foot[-1]:
				temp=valid(each,board)
				for tp in temp:
					if tp not in next:
						next.append(tp)
						board[tp[0]][tp[1]]=time
		foot.append(next)
		time+=1
		logging.info('time %s' % time)
		logging.info('next %s' % next)
		logging.info(board)
			
	return time-1 	
			
	
	
# TEST CASE --> PASSED ALL THE CASES
knight('a1','f1')	# 3
