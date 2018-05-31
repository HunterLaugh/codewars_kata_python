# coding:utf-8
'''
Mystery Function
The mystery function is defined over the non-negative integers. The more common name of this function is concealed in order to not tempt you to search the Web for help in solving this kata, which most definitely would be a very dishonorable thing to do.

Assume num has n bits. Then mystery(num) is the number whose binary representation is the num'th entry in the table T(n), where T(n) is defined recursively as follows:

T(1) = ['0', '1']

T(n + 1) is obtained by taking two copies of T(n), reversing the second copy, prepending each entry of the first copy with '0' and each entry of the reversed copy with '1', and then concatenating the two. For example:

T(2) = ['00', '01', '11', '10']

and

T(3) = ['000', '001', '011', '010', '110', '111', '101', '100']

mystery(6) is the 6'th entry in T(3)(with indexing starting at 0), i.e., '101' interpreted as a binary number. So, mystery(6) returns 5.

Your mission is to implement the functionmystery, where the argument may have up to 63 bits. Note that T(63) is far too large to compute and store, so you'll have to find an alternative way of implementing mystery. You are also asked to implement mystery_inv (JS mysteryInv), the inverse of mystery. Finally, you are asked to implement a function name_of_mystery (JS nameOfMystery), which shall return the name that mystery is more commonly known as. After passing all tests you are free to learn more about this function on Wikipedia or other place.

Hint: If you don't know the name of mystery, remember there is information in passing as well as failing a test.
'''
# T(n)为n位数二进制，由0,1组成，如T(1)=['0','1'];T(2)=['00', '01', '11', '10'];T(3) = ['000', '001', '011', '010', '110', '111', '101', '100']
# T(n)=T(1)*T(n-1)的组合，当T(n-1）
# mystery(n)为T()中下标为n的值，下值由0开始

def getCount(n):
	i=1
	while 2**i<=n:
		i+=1
	return i

def T(count):
	base=('0','1')
	t1=['0','1']
	print(t1)
	t2=[]
	i=2
	while i<=count:
		j=0
		while j<len(t1):
			if j%2==0:
				t2.append(t1[j]+base[0])
				t2.append(t1[j]+base[1])
			else:
				t2.append(t1[j]+base[1])
				t2.append(t1[j]+base[0])
			j+=1
		t1=t2
		print(t1)
		t2=[]
		i+=1
	return t1

def mystery(n):
	count=getCount(n)
	t=T(count)
	nTh=t[n]
	nLen=len(nTh)
	sum=0
	i=1
	for each in nTh:
		sum+=int(each)*2**(nLen-i)
		i+=1
	return sum


def decodeChangeBinary(n):
	binary=[]
	while (n//2)>0:
		binary.insert(0,str(n%2))
		n=n//2
	binary.insert(0,str(n))
	return ''.join(binary)
	
def mystery_inv(n):
	binary=decodeChangeBinary(n)
	count=len(binary)
	t_list=T(count)
	nTh=t_list.index(binary)
	return nTh
	
mystery_inv(5)

def name_of_mystery():
    pass
	
# TEST CASE PASSED BASIC CASE  BUG TIME OUT 
'''
test.assert_equals(mystery(6), 5, "mystery(6) ")
test.assert_equals(mystery_inv(5), 6, "mystery_inv(5)")
test.assert_equals(mystery(9), 13, "mystery(9) ")
test.assert_equals(mystery_inv(13), 9, "mystery_inv(13)")
test.assert_equals(mystery(19), 26, "mystery(19) ")
test.assert_equals(mystery_inv(26), 19, "mystery_inv(26)")
'''