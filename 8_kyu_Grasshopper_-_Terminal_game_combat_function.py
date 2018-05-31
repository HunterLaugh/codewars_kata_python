'''
8 kyu
Grasshopper - Terminal game combat function
Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.
'''

def combat(helth,damage):
	res=helth-damage
	if res<0:
		res=0
	
	return res