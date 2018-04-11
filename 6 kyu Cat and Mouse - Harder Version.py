'''
Cat and Mouse - Harder Version
You will be given a string (x) featuring a cat 'C', a dog 'D' and a mouse 'm'. The rest of the string will be made up of '.'.
You need to find out if the cat can catch the mouse from it's current position. The cat can jump (j) characters.
Also, the cat cannot jump over the dog.
So:
if j = 5:
..C.....m. returns 'Caught!' <-- not more than j characters between
.....C............m...... returns 'Escaped!' <-- as there are more than j characters between the two, the cat can't jump far enough
if j = 10:
...m.........C...D returns 'Caught!' <--Cat can jump far enough and jump is not over dog
...m....D....C....... returns 'Protected!' <-- Cat can jump far enough, but dog is in the way, protecting the mouse
Finally, if all three animals are not present, return 'boring without all three'
'''
# pass all case in codewars

# cat jump right/left
def cat_mouse(x,j):
	cat=-1
	if 'C' in x:
		cat=x.index('C')
	
	mouse=-1
	if 'm' in x:
		mouse=x.index('m')
	
	dog=-1
	if 'D' in x:
		dog=x.index('D')
	
	if cat==-1 or mouse==-1 or dog==-1:
		return 'boring without all three'
		
	
	if cat>mouse:
		dis=cat-mouse-1
	else:
		dis=mouse-cat-1
		
	if dis<=j:
		if cat>dog>mouse or  cat<dog<mouse:
			return 'Protected!'
		return 'Caught!'
	else:
		return 'Escaped!'