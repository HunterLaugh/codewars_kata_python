def reverse_words(text):
	res=[]
	i=0
	temp=[]
	while i<len(text):
		if text[i]!=' ':
			temp.append(text[i])
		elif text[i]==' ' and temp:
			p=temp[::-1]
			l=''.join(p)
			res.append(l)
			res.append(' ')
			temp=[]
		else:
			res.append(' ')
		i+=1
	if temp:
		p=temp[::-1]
		l=''.join(p)
		res.append(l)
	
	return ''.join(res)

	
# TEST CASE  --> PASSED ALL THE CASES
t1='this is  john!'
print(reverse_words(t1))

	