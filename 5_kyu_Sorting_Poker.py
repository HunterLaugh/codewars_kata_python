'''
Sorting Poker
Description:

John learns to play poker with his uncle. His uncle told him: Poker to be in accordance with the order of "2 3 4 5 6 7 8 9 10 J Q K A". The same suit should be put together. But his uncle did not tell him the order of the four suits.

Give you John's cards and Uncle's cards(two string john and uncle). Please reference to the order of Uncle's cards, sorting John's cards.
Examples

sortPoker("♦6♥2♠3♦5♠J♣Q♠K♣7♦2♣5♥5♥10♠A","♠2♠3♠5♥J♥Q♥K♣8♣9♣10♦4♦5♦6♦7")
should return: "♠3♠J♠K♠A♥2♥5♥10♣5♣7♣Q♦2♦5♦6"

sortPoker("♦6♥2♠3♦5♠J♣Q♠K♣7♦2♣5♥5♥10♠A","♣8♣9♣10♦4♦5♦6♦7♠2♠3♠5♥J♥Q♥K")
should return: "♣5♣7♣Q♦2♦5♦6♠3♠J♠K♠A♥2♥5♥10"


For Python:

Suits are defined as S, D, H, C.

sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","S2S3S5HJHQHKC8C9C10D4D5D6D7")
should return "S3SJSKSAH2H5H10C5C7CQD2D5D6"
sort_poke("D6H2S3D5SJCQSKC7D2C5H5H10SA","C8C9C10D4D5D6D7S2S3S5HJHQHK") 
should return "C5C7CQD2D5D6S3SJSKSAH2H5H10"

'''
# 输入：John的牌，Uncle的牌
# 输出：John的牌按照Uncle的排序输出，1 花色顺序  2 "2 3 4 5 6 7 8 9 10 J Q K A"顺序
# 思路：先排花色，再排序
# 先求出Uncle的花色
# tag

def sort_poker(john, uncle):
	spades=[]    #黑桃	S
	hearts=[]    #红桃	H
	clubs=[]	 #梅花	C
	diamonds=[]	 #方片	D
	
	uncle_li=list(uncle)
	seq=[]
	
	# Uncle花色顺序
	for each in uncle_li:
		if each in 'SHCD':
			if each not in seq:
				seq.append(each)
	print(seq)
	
	# 分离
	n=len(john)
	i=0
	while i<n-1:
		each0=john[i]
		each1=john[i+1]
		
		if each0 not in 'SHCD':
			i+=1
			continue
		
		if each0=='S':
			if each1!='1':
				spades.append(each1)
			else:
				spades.append('10')
		elif each0=='H':
			if each1!='1':
				hearts.append(each1)
			else:
				hearts.append('10')
		elif each0=='C':
			if each1!='1':
				clubs.append(each1)
			else:
				clubs.append('10')
		elif each0=='D':
			if each1!='1':
				diamonds.append(each1)
			else:
				diamonds.append('10')	
		
		i+=1

	# 按点数排好序，合成字符串
	print(spades,clubs,hearts,diamonds)
	
	sp='S'+'S'.join(seq_tag(spades))
	he='H'+'H'.join(seq_tag(hearts))
	cl='C'+'C'.join(seq_tag(clubs))
	di='D'+'D'.join(seq_tag(diamonds))



	temp=['S',sp,'H',he,'C',cl,'D',di]
	
	res=[]
	# 按花纹排序
	for each in seq:
		res.append(temp[temp.index(each)+1])

	return ''.join(res)
	
# L 输入扑克字符list，return 排好序的字符list	
# list.index(obj)  返回obj的下标索引
def seq_tag(L):
	tag=['N','N','N','N','N','N','N','N','N','N','N','N','N',]
	pokerSort=['2','3','4','5','6','7','8','9','10','J','Q','K','A']

	# 如有扑克牌，则tag为'Y'
	for each in L:
		if each in pokerSort:
			index=pokerSort.index(each)
			tag[index]='Y'

	res=[]
	i=0
	while i<13:
		if tag[i]=='Y':
			res.append(pokerSort[i])
		i+=1	

	return res

print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","S2S3S5HJHQHKC8C9C10D4D5D6D7"))





