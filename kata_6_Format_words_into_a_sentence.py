'''
Format words into a sentence
Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned.

formatWords(['ninja', 'samurai', 'ronin']) // should return "ninja, samurai and ronin"
formatWords(['ninja', '', 'ronin']) // should return "ninja and ronin"
formatWords([]) // should return ""

'''

def format_words(words):
	if not words:
		return ""
		
	L=[]
	for each in words:
		if each:
			L.append(each)
	
	if not L:
		return ""
	
	n=len(L)
	if n==1:
		return L[0]
	elif n==2:
		return L[0]+' and '+L[1]
	else:
		i=0
		while i<n-2:
			L[i]=L[i]+','
			i+=1
		L.insert(n-1,'and')
		return ' '.join(L)
		
l=['one','two', 'three','four']
print(format_words(l))
		
			