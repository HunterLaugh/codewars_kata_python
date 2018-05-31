'''
Bouncing Balls
A child plays with a ball on the nth floor of a big building. The height of this floor is known.

(float parameter "h" in meters. Condition 1) : h > 0)

He lets out the ball. The ball bounces for example to two-thirds of its height.

(float parameter "bounce". Condition 2) : 0 < bounce < 1)

His mother looks out of a window that is 1.5 meters from the ground.

(float parameters "window". Condition 3) : window < h).

How many times will the mother see the ball either falling or bouncing in front of the window?

If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note

You will admit that the ball can only be seen if the height of the rebouncing ball is stricty greater than the window parameter.

Example:

    h = 3, bounce = 0.66, window = 1.5, result is 3

    h = 3, bounce = 1, window = 1.5, result is -1 (Condition 2) not fulfilled).


'''
def bouncingBall(h, bounce, window):
	if h>0 and bounce>0 and bounce<1 and window<h and window>0:
		times=0
		while h>=window:
			times+=1
			h=h*bounce
			if h>=window:
				times+=1
		return times
	else:
		return -1
		
# 	TEST CASE	PASSED ALLD THE CASE
print(bouncingBall(3,0.66,1.5))    # 3
print(bouncingBall(30,0.66,1.5))    # 15
		
		