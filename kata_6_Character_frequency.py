'''
Character frequency
Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. This count excludes numbers, spaces and all punctuation marks. Upper and lower case versions of a character are equivalent and the result should all be in lowercase.

The function should return a list of tuples (in Python) or arrays (in other languages) sorted by the most frequent letters first. The Rust implementation should return an ordered BTreeMap. Letters with the same frequency are ordered alphabetically. For example:

  letter_frequency('aaAabb dddDD hhcc')

will return

  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]

Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher.
'''
# coding:utf-8
# 统计字符出现次数，大小写算1样的，以（小写，次数）的元组形式输出
# 排序方式：1 次数，由大到小 ，2 若次数相同-则按字母由a--z的顺序
def letter_frequency(text):
	l=list(text)
	alphabet=[]
	# alphabet 
	for each in l:
		if ( ord(each)>=ord('A') and ord(each)<=ord('Z') ) or ( ord(each)>=ord('a') and ord(each)<=ord('z') ):
			alphabet.append(each.lower())
	
	m=set(alphabet)
	res=[]
	# count every letter appear time 
	for letter in m:
		time=alphabet.count(letter)
		res.append((letter,time))
		
	# sort
	length=len(res)
	i=0
	while i<len(res)-1:
		max=i
		j=i+1		
		while j<len(res):
			if res[j][1]>res[max][1] or ( res[j][1]==res[max][1] and ord(res[j][0])<ord(res[max][0]) ):
				max=j
			j+=1
		if max>i:
			temp=res[i]
			res[i]=res[max]
			res[max]=temp
		i+=1
		
	return res
				
			
					

	
			

	



