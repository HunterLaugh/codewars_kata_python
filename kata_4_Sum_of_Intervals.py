'''
Sum of Intervals
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
Overlapping Intervals

List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]

The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
Examples

sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19

'''

def sum_of_intervals(intervals):
#	for each in intervals:
#		each.sort()
	intervals.sort()
	
	i=0
	while i<len(intervals)-1:
		j=i+1
		while j<len(intervals):
			l1,r1=intervals[i]
			l2,r2=intervals[j]
			if l2>r1:
				i+=1
				break
			elif (l2>=l1 and l2<=r1) and (r2>=l1 and r2<=r1):
				intervals.pop(j)
			elif (l2>=l1 and l2<=r1) and (r2>r1):
				intervals[i]=[l1,r2]
				intervals.pop(j)
			else:
				i+=1
				break
	
	res=0
	for each in intervals:
		l,r=each
		res+=(r-l)
	return res
	
# TEST --> PASSED ALL THE CASES
data=[
		[1,5],
		[10, 20],
		[1, 6],
		[16, 19],
		[5, 11]
	  ]  				# ==> 19
	  
sum_of_intervals(data)
sum_of_intervals( [
   [1,2],
   [6, 10],
   [11, 15]
] )					# // => 9

sum_of_intervals( [
   [1,4],
   [7, 10],
   [3, 5]
] )					# // => 7

sum_of_intervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] )					# // => 19