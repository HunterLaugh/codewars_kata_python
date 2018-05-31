'''
Converting Measures
Mary wrote a recipe book and is about to publish it, but because of a new European law, she needs to update and include all measures in grams.

Given all the measures in tablespoon (tbsp) and in teaspoon (tsp), considering 1 tbsp = 15g and 1 tsp = 5g, append to the end of the measurement the biggest equivalent integer (rounding up).
Examples

"2 tbsp of butter"    -->  "2 tbsp (30g) of butter"

"1/2 tbsp of oregano" -->  "1/2 tbsp (8g) of oregano"

"1/2 tsp of salt"     -->  "1/2 tbsp (3g) of salt"

"Add to the mixing bowl and coat well with 1 tbsp of olive oil & 1/2 tbsp of dried dill" -->
"Add to the mixing bowl and coat well with 1 tbsp (15g) of olive oil 

'''

# regular expression

import re

# TEST CASE   PASSED ALL
a='2 tbsp of butter'      
#"2 tbsp (30g) of butter"

b="Add to the mixing bowl and coat well with 1 tbsp of olive oil & 1/2 tsp of dried dill"  
# "Add to the mixing bowl and coat well with 1 tbsp (15g) of olive oil & 1/2 tsp (8g) of dried dill"

def convert_recipe(recipe):
	pattern=re.compile(r'([0-9/]+) (tbsp|tsp)')
	match=pattern.findall(recipe)
	change_dict={'tbsp':15,'tsp':5}
	for each in match:
		if '/' not in each[0]:
			temp=int(each[0])*change_dict[each[1]]
		else:
			pat_int=re.compile(r'([0-9]+)/([0-9]+)')
			ea_int=pat_int.findall(each[0])
			temp=int(ea_int[0][0])*change_dict[each[1]]/int(ea_int[0][1])
			if int(temp)+0.00<temp:
				temp=int(temp)+1
			else:
				temp=int(temp)
		
		old=each[0]+' '+each[1]
		new=old+' ('+str(temp)+'g)'
		recipe=recipe.replace(old,new,1)	
		
	return recipe




print(convert_recipe(a))



