'''
8kyu interpreters HQ9+
You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:

    If the input is 'H', return 'Hello World!'
    If the input is 'Q', return the input
    If the input is '9', return the full lyrics of 99 Bottles of Beer. It should be formatted like this:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
...
...
...
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

    For everything else, don't return anything (return null in C#).

(+ has no visible effects so we can safely ignore it.)
'''

def HQ9(code):
	res=''
	i=99
	
	if code=='H':
		res='Hello World!'
	elif code=='Q':
		res='Q'
	elif code=='9':
		res="%d bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, %d bottles of beer on the wall.,% (i,i-1)"
		i=i-1
	else:
		res=None
		
	return res