'
You have invented a time-machine which has taken you back to ancient Rome. Caeser is impressed with your programming skills and has appointed you to be the new information security officer.

Caeser has ordered you to write a Caeser cipher to prevent Asterix and Obelix from reading his emails.

A Caeser cipher shifts the letters in a message by the value dictated by the encryption key. Since Caeser's emails are very important, he wants all encryptions to have upper-case output, for example:

If key = 3 "hello" -> KHOOR If key = 7 "hello" -> OLSSV

Input will consist of the message to be encrypted and the encryption key.
'


def caeser(message, key):
	base='abcdefghijklmnopqrstuvwxyz'
	res=[]
	
	for each in message:
		if (ord(each)>=ord('A') and ord(each)<=ord('Z')) or (ord(each)>=ord('a') and ord(each)<=ord('z')):
			idx=base.index(each.lower())+key
			new=(base[idx%26]).upper()
			res.append(new)
		else:
			res.append(each)
	return ''.join(res)
	

# PASSED ALL THE CASES