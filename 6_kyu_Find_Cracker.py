'''
Find Cracker
Someone was hacking the score. Each student's record is given as an array The objects in the array are given again as an array of scores for each name and total score. ex>

array = [
["name1", 445, ["B", "A", "A", "C", "A", "A"]],
["name2", 140, ["B", "A", "A", "A"]],
["name3", 200, ["B", "A", "A", "C"]]
]

The scores for each grade is:

    A: 30 points
    B: 20 points
    C: 10 points
    D: 5 points
    Everything else: 0 points

If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score should be capped at 200 points.

Returns the name of the hacked name as an array when scoring with this rule.

var array = [
["name1", 445, ["B", "A", "A", "C", "A", "A"]], # name1 total point is over 200 => hacked
["name2", 140, ["B", "A", "A", "A"]], #  name2 point is right
["name3", 200, ["B", "A", "A", "C"]] # name3 point is 200 but real point is 90 => hacked
];

return ["name1", "name2"]


'''

# not pass the case 
def find_hack(arr):
	hk_name=[]
	for each in arr:
		name=each[0]
		score=each[1]
		grades=each[2]
		
		isAB=True	
		sum=0
		for grd in grades:
			sum+=grade_score(grd)
			if grd not in 'AB':
				isAB=False
		
		if isAB and len(grades)>=5:
			sum+=20
		
		if sum!=score:
			hk_name.append(name)
	
	return hk_name
				
	
def grade_score(word):
	res=0
	di={'A':30,'B':20,'C':10,'D':5}
	if word in 'ABCD':
		res=di[word]
	return res