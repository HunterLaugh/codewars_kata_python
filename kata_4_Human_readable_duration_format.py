'''
Human readable duration format
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
	if seconds==0:
		return 'now'
	
	year_second=365*24*60*60
	day_second=24*60*60
	hour_second=60*60
	minute_second=60
	
	year,day,hour,minute=[0,0,0,0]
	
	res=[]
	if seconds>=year_second:
		year=seconds//year_second
		if year==1:
			res.append('1 year')
		else:
			res.append(str(year)+' years')
		seconds=seconds-year*year_second
	
	if seconds>=day_second:
		day=seconds//day_second
		if day==1:
			res.append('1 day')
		else:
			res.append(str(day)+' days')
		seconds=seconds-day*day_second
	
	if seconds>=hour_second:
		hour=seconds//hour_second
		if hour==1:
			res.append('1 hour')
		else:
			res.append(str(hour)+' hours')
		seconds=seconds-hour*hour_second
		
	if seconds>=minute_second:
		minute=seconds//minute_second
		if minute==1:
			res.append('1 minute')
		else:
			res.append(str(minute)+' minutes')
		seconds=seconds-minute*minute_second

	if seconds==0:
		pass		
	elif seconds==1:
		res.append('1 second')
	else:
		res.append(str(seconds)+' seconds')	
		
	print(res)
	long=len(res)
	if long==1:
		format=res[0]
	elif long==2:
		format=res[long-2]+' and '+res[long-1]
	else:
		format=', '.join(res[:long-2])+', '+res[long-2]+' and '+res[long-1]
	print(format)
	return format
	

# TEST CASE	--> PASSED ALL THE CASES
format_duration(1) 		# "1 second"
format_duration(62) 		#"1 minute and 2 seconds"
format_duration(120) 		#"2 minutes"
format_duration(3600) 		#"1 hour"
format_duration(3662) 		#"1 hour, 1 minute and 2 seconds"