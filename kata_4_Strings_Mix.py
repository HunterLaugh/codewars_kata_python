'''
Strings Mix
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

Note for Swift, R

The prefix =: is replaced by E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
'''
# input: string s1,s2 --> count lowercase --> compare length lowercase --> sort:1. length ,2. the same length -- alpha's ascii -->output: "1or2or=:lowercase/./././:
def mix(s1, s2):
	# get lowercase
	L1=[]
	for each in s1:
		if each.islower():
			L1.append(each)
	L2=[]
	for each in s2:
		if each.islower():
			L2.append(each)
	
	# set
	setL1=set(L1)
	setL2=set(L2)
	
	# count
	countS1={}
	countS2={}
	for l1 in setL1:
		c1=L1.count(l1)
		if c1>1:
			countS1[l1]=[0,c1]
	for l2 in setL2:
		c2=L2.count(l2)
		if c2>1:
			countS2[l2]=[0,c2]	

	# compare
	MAX={}
	for key in countS1:
		v1=countS1[key][1]
		if key not in countS2:
			MAX[key]=[1,v1]
		else:
			v2=countS2[key][1]
			if v1>v2:
				MAX[key]=[1,v1]
			elif v1<v2:
				MAX[key]=[2,v2]
			else:
				MAX[key]=['=',v1]
	for otherkey in countS2:
		if otherkey not in MAX:
			MAX[otherkey]=[2,countS2[otherkey][1]]
	print(MAX)
	
	# sort
	SORT=[]
	while MAX:
		for first in MAX:
			idx=first
			break
		for each in MAX:
			if each==idx:
				pass
			elif MAX[each][1]>MAX[idx][1]:
				idx=each
			elif MAX[each][1]==MAX[idx][1]:
				some=[1,2,'=']
				if some.index(MAX[each][0])<some.index(MAX[idx][0]):
					idx=each
				elif some.index(MAX[each][0])==some.index(MAX[idx][0]):
					if ord(each)<ord(idx):
						idx=each
				else:
					pass
			else:
				pass
		flag=MAX[idx][0]
		if flag!='=':
			flag=str(flag)
		count=MAX[idx][1]
		s=idx*count
		SORT.append(flag+':'+s)
		del MAX[idx]
	
	res='/'.join(SORT)
	print(res)
	return res	
	
		
	
# TEST CASE	-->PASSED ALL THE CASES
s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) 	#--> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"