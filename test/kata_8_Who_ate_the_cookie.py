'''
8 kyu
Who ate the cookie
For this problem you must create a program that says who ate the last cookie. 
If the input is a string then "Zach" ate the cookie. 
If the input is a float or an int then "Monica" ate the cookie. 
If the input is anything else "the dog" ate the cookie. 
The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "It was Monica" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.
'''

def cookie(x):
	x_type=type(x)
	res=''
	
	if x_type==str :
		res="Who ate the last cookie? It was Zach!"
	elif x_type==int or x_type==float:
		res="Who ate the last cookie? It was Monica!"
	else:
		res="Who ate the last cookie? It was the dog!"
		
	return res