# coding:utf-8
'''
Traffic Jam
Story

Well, here I am stuck in another traffic jam.

Damn all those courteous people!

Cars are trying to enter the main road from side-streets somewhere ahead of me and people keep letting them cut in.

Each time somebody is let in the effect ripples back down the road, so pretty soon I am not moving at all.

(Sigh... late again...)
Visually

The diagram below shows lots of cars all attempting to go North.

    the a,b,c... cars are on the main road with me (X)
    the B cars and C cars are merging from side streets

          |  a  |   
          |  b  | ↑  
  --------+  c  |  
     BBBBBB  d  |   
  --------+  e  |  
          |  f  | ↑
          |  g  |   
  --------+  h  |
      CCCCC  i  |
  --------+  j  | ↑
          |  k  |
          |  l  |
          |  m  |
          |  X  | 

This can be represented as

    mainRoad = "abcdefghijklmX"
    sideStreets = ["","","","BBBBBB","","","","","CCCCC"]

Kata Task

Assume every car on the main road will "give way" to 1 car entering from each side street.

Return a string representing the cars (up to and including me) in the order they exit off the top of the diagram.
Notes

    My car is the only X, and I am always on the main road
    Other cars may be any alpha-numeric character (except X of course)
    There are no "gaps" between cars
    Assume side streets are always on the left (as in the diagram)
    The sideStreets array length may vary but is never more than the length of the main road
    A pre-loaded Util.display(mainRoad,sideStreets) method is provided which may help to visualise the data

Example

Here are the first few iterations of my example, showing that I am hardly moving at all...
Initial	Iter 1	Iter 2	Iter 3	Iter 4	Iter 5	Iter 6	Iter 7

      a
      b
      c
BBBBBBd
      e
      f
      g
      h
 CCCCCi
      j
      k
      l
      m
      X 

	

      b
      c
      d 
 BBBBBB
      e
      f
      g
      h
 CCCCCi
      j
      k
      l
      m
      X

	

      c
      d
      B
 BBBBBe
      f
      g
      h
      i
  CCCCC
      j
      k
      l
      m
      X

	

       d
       B
       e
   BBBBB
       f
       g
       h
       i
   CCCCC
       j
       k
       l
       m
       X

	

     B
     e
     B
 BBBBf
     g
     h
     i
     C
 CCCCj
     k
     l
     m
     X

	

     e
     B
     f
  BBBB
     g
     h
     i
     C
 CCCCj
     k
     l
     m
     X

	

     B
     f
     B
  BBBg
     h
     i
     C
     j
  CCCC
     k
     l
     m
     X

	

     f
     B
     g
   BBB
     h
     i
     C
     j
  CCCC
     k
     l
     m
     X

:-)

DM


'''

'''
有趣的问题，贴近生活

输入：主路车、支路车
过程：主路往北开，主路每移动1步，开出去1辆车，从支路汇入1台车，
	支路依次汇入
输出：当X车开出主路时，已开出主路的车
 return run away car's name 
'''
 # not pass the test case
 
def traffic_jam(main_road, side_streets):
	lst_main_road=list(main_road)
	N=len(lst_main_road)
	res=[]
	
	pool=[]
	temp=0
	while temp<len(side_streets):
		if side_streets[temp]:
			pool.append(temp)
		temp+=1
	tpl_pool=tuple(pool)	#街道位置
	
	maxStreetCar=max(map(len,side_streets))
		
	step=0 #每1次进1辆车
	j=0    #街上的车
	while j<maxStreetCar:
		i=0    #第几条街
		while i<len(tpl_pool):
			try:
				street=tpl_pool[i]
				car=side_streets[street][j]
				lst_main_road.insert(street+1,car)
			except IndexError:
				pass
			finally:
				if len(lst_main_road)>N:
					res.append(lst_main_road[0])
					lst_main_road.pop(0)
					step+=1
					print('step',step)
					print('lst_main_road',lst_main_road)
					print()
					
				if res[-1]=='X':
					print('step',step)
					return ''.join(res)
				i+=1
		
		j+=1


main_road_test_value="abcdeXghi"
side_streets_test_value=["","","CCCCC","","EEEEEEEEEE","FFFFFF","","",""]
print(traffic_jam(main_road_test_value,side_streets_test_value))

'''
test case 

Test.describe("Sample tests")

Test.it("Give way")
test.assert_equals(traffic_jam("abcdeXghi", ["","","CCCCC","","EEEEEEEEEE","FFFFFF","","","IIIIII"]), "abcCdCeCECX")

print("<COMPLETEDIN::>")


Test.it("No side streets")
test.assert_equals(traffic_jam("abcdefX", []), "abcdefX")
test.assert_equals(traffic_jam("abcXdef", []), "abcX")
test.assert_equals(traffic_jam("Xabcdef", []), "X")

print("<COMPLETEDIN::>")


Test.it("example")
test.assert_equals(traffic_jam("abcdefghijklmX", ["","","","BBBBBB","","","","","CCCCC"]), "abcdBeBfBgBhBiBCjCkClCmCX")

print("<COMPLETEDIN::>")
print("<COMPLETEDIN::>")

'''

