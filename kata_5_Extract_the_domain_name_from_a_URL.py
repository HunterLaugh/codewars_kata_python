'''
Extract the domain name from a URL
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''
import re
def domain_name(url):
	pattern=re.compile(r'(?:https?://)?w{0,3}\.?([\da-zA-Z-]{2,30})\.')
	result=pattern.search(url)
	domain=result.group(1)
	print(domain)
	return domain
	

# TEST CASE  --> PASSED ALL THE CASES
domain_name("http://github.com/carbonfive/raygun")	# == "github" 
domain_name("http://www.zombie-bites.com") 	#== "zombie-bites"
domain_name("https://www.cnet.com") 	#== "cnet"