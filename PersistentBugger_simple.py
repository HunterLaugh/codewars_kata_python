def persistence(n):
	count=0
	while n>=10:
		temp=1
		L=list(str(n))
		for x in L:
			temp=int(x)*temp
		n=temp
		count=count+1
	
	return count
	
print("persistence(2)",persistence(2))
print("persistence(29)",persistence(29))		
print("persistence(398)",persistence(398))
print("persistence(7892)",persistence(7892))
print("persistence(98772)",persistence(98772))