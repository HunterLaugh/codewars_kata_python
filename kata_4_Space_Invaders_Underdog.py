'''
Space Invaders Underdog
This kata is inspired by Space Invaders (Japanese: スペースインベーダー), an arcade video game created by Tomohiro Nishikado and released in 1978.

Alien invaders are attacking Earth and you've been conscripted to defend.
The Bad News: You performed poorly in the manual training. As a result, you're ranked low priority and you're piloting a space jalopy.
The Good News: Your coding skill is better than your piloting and you know the movement pattern of the alien spaceships.

You're going to program an algorithm that aids in shooting down the incoming alien wave despite your limitations.

Input

The action takes place on an m x n matrix. Your function will receive two arguments:

    a 2-D array where each subarray represents a row of alien ships. Subarrays consist of integers that represent each alien ship. Zero values (0) are empty spaces.
    your [row,column] coordinates

The width (n) of a row is equal to the length of a subarray in the first argument and all rows are of the same length.
Your row coordinate will be the last row of the matrix (m - 1).

Alien Ship Movement Pattern

    Each alien ship is given in the form of an integer that represents its movement speed and direction.
    Alien ships move left or right. A positive integer means an alien moves right, a negative integer means an alien moves left. The absolute value of the integer is the distance the alien moves in 1 turn.
    When an alien reaches an edge, it moves down one position and reverses lateral (left/right) direction.

Your Ship's Limitations

    Your position is fixed.
    Your pulse cannon has a time delay of 1 turn. After the delay, your cannon blasts the first target in its path.
    You can fire up to one shot per turn.

Output

Your function should return an array of integers. Each integer represents the turn for each shot fired from your ship's cannon. If it is not possible to destroy all alien ships before they reach the last row, return null or None.

Test Example

state 0

Above: Turn 0 (Initial State)
Below: Turn 1
state 1

The images above represent the matrix states at Turn 0 and Turn 1 for the test example below. Note the following:

    Multiple alien ships can occupy the same space concurrently. The red alien at [0,2] and the light blue alien at [0,7] at turn 0 will both end up at position [0,4] at turn 1.
    The pink alien (1) at [0,9] at turn 0 is already at the right edge, so it moves one space down and changes direction from right to left.
    The yellow alien (6) at [0,6] at turn 0 ends up at [1,7] at turn 1.
    The green alien (7) at [0,8] at turn 0 ends up at [1,4] (white alien) and gets shot down by your cannon at turn 1. Therefore, the time of registering your first shot is at turn 0.

In the test example, there is only one subarray in the first argument, meaning only the top row (row 0) of the matrix is occupied at the initial state.

alien_wave = [[3,1,2,-2,2,3,6,-3,7,1]]
position = [6,4]

blast_sequence(alien_wave,position)# [0, 2, 3, 4, 5, 9, 10, 13, 19, 22]

Other Technical Details

    In the event where multiple alien ships occupy the same position and the position is the target of your cannon fire, the fastest alien ship will be destroyed. If two ships are going at the same speed in opposite directions, the ship moving to the right will be destroyed.
    All alien ship movement speeds will be less than the width of the matrix.
    Alien count upper bound is 228
    Inputs will always be valid

If you enjoyed this kata, be sure to check out my other katas.
Algorithms
Games
'''
import logging
logger=logging.getLogger()
logger.setLevel(10)

def move(speed,coord,length,width):
	row,column=coord
	column=column+speed
	if column>width-1:
		row+=1
		column=width*2-column-1
		speed=-speed
	elif column<0:
		row+=1
		column=-column-1
		speed=-speed
	else:
		pass
	logging.debug('speed %s, row %s, column %s' % (speed,row,column))
	return [speed,row,column]
	
def blast_sequence(aliens,position):
	M=position[0]+1
	N=len(aliens[0])
	logging.debug('M %s' % M)
	logging.debug('N %s' % N)
	
	coordinate=[]
	for each in aliens:
		temp=[]
		for idx in range(N):
			temp.append(idx)
		coordinate.append(temp)
	logging.debug(coordinate)
	
	turn=0
	while 

# TEST CASE
example_aliens = [
	[[3,1,2,-2,2,3,6,-3,7,1]],
	[[5,2,-2,3,1,0,4,8,3,-2,5],[1,4,-1,0,3,6,1,-3,1,2,-4]],
	[[4,1,-7,-5,1,6,3,-2,1,0,2,6,5],[2,0,3,-4,0,2,-1,5,-8,-3,-2,-5,1],[1,2,0,-6,4,7,-2,4,-4,2,-5,0,4]]]
example_positions = [[6,4],[10,2],[15,6]]
example_solutions = [
	[0,2,3,4,5,9,10,13,19,22],
	[1,4,5,6,8,9,10,12,14,15,16,18,19,20,21,26,27,30,32,36],
	[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,21,22,23,25,27,30,31,32,35,36,38,40,43,45,56,58]]

for aliens,pos,sol in zip(example_aliens,example_positions,example_solutions):
	blast_sequence(aliens,pos)
