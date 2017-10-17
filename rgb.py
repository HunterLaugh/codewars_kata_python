"""
RGB To Hex Conversion

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

# coding:utf-8
# 十进制转十六进制  hex(number)

def rgb(r,g,b):
	if r<0:
		r=0
	if r>255:
		r=255
		
	if g<0:
		g=0
	if g>255:
		g=255
		
	if b<0:
		b=0
	if b>255:
		b=255
		
	hexRgb=list(map(hex,[r,g,b]))
	
	i=0
	while i<3:
		# 如果没有4位，在第3位补0
		if len(hexRgb[i])<4:
			temp=list(hexRgb[i])
			temp.insert(2,'0')
			hexRgb[i]="".join(temp)
		
		i+=1

	re=hexRgb[0][2:]+hexRgb[1][2:]+hexRgb[2][2:]
	RE=re.upper()
	return RE

print(rgb(255,255,255))
print(rgb(1,2,3))
print(rgb(0,0,0))