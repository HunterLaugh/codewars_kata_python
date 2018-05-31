'''
8 kyu
Calculate BMI
Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

def bmi(weight,height):
	if height==0 or weight==0:
		return 'Error'
		
	bmi=weight/(height*height)
	res=''
	
	if bmi>30:
		res='Obese'
	elif bmi<=30.0 and bmi>25.0:
		res='Overweight'
	elif bmi<=25.0 and bmi>18.5:
		res='Normal'
	else :
		res='Underweight'
		
	return res
		