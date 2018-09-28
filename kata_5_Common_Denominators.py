'''
Common Denominators
Common denominators

You will have a list of rationals in the form

 { {numer_1, denom_1} , ... {numer_n, denom_n} }

or

 [ [numer_1, denom_1] , ... [numer_n, denom_n] ]

or

 [ (numer_1, denom_1) , ... (numer_n, denom_n) ]

where all numbers are positive ints.

You have to produce a result in the form

 (N_1, D) ... (N_n, D)

or

 [ [N_1, D] ... [N_n, D] ]

or

 [ (N_1', D) , ... (N_n, D) ]

or

{{N_1, D} ... {N_n, D}}

depending on the language (See Example tests)

in which D is as small as possible and

 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

Note for Bash

input is a string, e.g "2,4,2,6,2,8"

output is then "6 12 4 12 3 12"
'''

def convertFracts(lst):
	denom=[]
	for each in lst:
		denom.append(each[1])
	last=int(max(denom)**0.5)+1	
	comDenom=1
	i=2
	while i<=last:
		idx=0
		flag=0
		while idx<len(denom):
			if denom[idx]%i==0:
				denom[idx]=denom[idx]//i
				flag=1
			idx+=1
		if flag:
			comDenom*=i
		else:
			i+=1
			if i%2==0:
				i+=1
	for each in denom:
		comDenom*=each
	res=[]
	for each in lst:
		up=(comDenom//each[1])*each[0]
		res.append([up,comDenom])
	return res



# TEST CASE	---> PASSED ALL THE CASES
a = [[1, 2], [1, 3], [1, 4],[1,5],[1,6]]
b = [[6, 12], [4, 12], [3, 12]]
convertFracts(a) 	#--> b
