'''
Count ones in a segment
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.

WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!

'''
def countOnes(left, right):
	a=list(map(bin,range(left,right+1)))
	b=list(map(count,a))
	for each in b:
		print(each)
	return sum(b)

def count(x):
	return x.count('1')

	
countOnes(1,3)

	
'''
# TEST CASE  运行超时  fail  怎么不遍历，而求解呢
# 使用排列组合的方式

def test(input,expect):
	if input==expect:
		print('YES')
	else:
		print('NO')

print(countOnes(5,200000000000000))
test(countOnes(5,10000),7)
test(countOnes(12,29),51)
'''