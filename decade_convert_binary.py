# decade >>> binary   use  recursion

def decade_convert_binary(num):
	binary=num%2
	if num>=2:
		decade_convert_binary(num//2)
	
	print(binary,end='')
	
decade_convert_binary(99)
print()