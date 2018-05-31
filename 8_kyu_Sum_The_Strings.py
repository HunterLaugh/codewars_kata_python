'''
8 kyu
Sum The Strings
Create a function that takes 2 numbers in form of a string as an input, and outputs the sum (also as a string):

  sumStr("4", "5")    // should output "9"
  sumStr("34", "5")   // should output "39"

If either input is an empty string, consider it as zero. If both inputs are empty, output "0".

HINT: Check these links out about parseInt() (Number() is also valid) and .toString(): https://www.w3schools.com/jsref/jsref_parseint.asp (NOTE: Radix is not necessary) https://www.w3schools.com/jsref/jsref_tostring_number.asp

'''
# if empty string is false

def sum_str(a,b):
	if a and b:
		return str(int(a)+int(b))
	elif not a and b:
		return b
	elif a and not b:
		return a
	elif not a and not b:
		return '0'

