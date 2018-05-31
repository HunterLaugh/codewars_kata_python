# coding:utf-8

'''
Helpers For a 3DGame I Biggest Triangle in a Sphere
For a new 3D game that will be released, a team of programmers needs an easy function. (Then it will be processed as a method in a Class, forget this concept for Ruby)

We have an sphere with center O, having in the space the coordinates [α, β, γ] and radius r and a list of points, points_list, each one with coordinates [x, y, z]. Select the biggest triangle (or triangles) that has (have) all its (their) 3 vertice(s) as interior points of the sphere (not even in the sphere contour). You should consider that a point P is interior if its distance to center O, d, is such that:

d < r and (d - r) / r| > 10-10

Let's see the situation with the following points in the image posted below:

A = [1,2,-4]; B = [-3, 2, 4]; C = [7, 8, -4]; D = [2, 3, 5]; E = [-2, -1, 1]

The sphere has the following features:

O = [1, 2, -2] (Center of the sphere)
radius = 8
As C is the only exterior point of the sphere, the possible triangles that have their vertices interior to the sphere are:

ABD, ABE, ADE, BDE

Let's see which is the biggest one:

Triangle    Triangle with its points         Area
ABD        [[1,2,-4],[-3,2,4],[2,3,5]]    22.44994432064
ABE        [[1,2,-4],[-3,2,4],[-2,-1,1]]  13.56465996625
ADE        [[1,2,-4],[2,3,5],[-2,-1,1]]   22.62741699796 <---- biggest triangle
BDE        [[-3,2,4],[2,3,5],[-2,-1,1]]   11.31370849898

Our function biggest_triang_int() (javascript: biggestTriangInt()should output for this case:

points_list = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
sphere_center = [1, 2, -2]
radius = 8
biggest_triang_int(points_list, sphere_center, radius) == [4, 22.62741699796,  [[1,2,-4],[2,3,5],[-2,-1,1]]]

That means that with the given points list we may generate 4 triangles with all their vertices as interior points of the sphere, the biggest triangle has an area of 22.62741699796 (the units does not matter and the values for the area should not be rounded) and finally, there is only one triangle with this maximum value. Every triangle should be output having the same order of its vertices than in the given list of points. B = [-3,2,4], comes before than D =[2,3,5] and the last one E = [-2,-1,1] If in the result we have only one triangle, the function should output a list of three points.

Let'see the next case:

points_list = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1],
              [3, 2, 6], [1, 4, 0], [-4, -5, -6], [4, 5, 6], [-2, -3, -5],
              [-1, -2, 4], [-3, -2, -6], [-1, -4, 0], [2, 1, -1]]
sphere_center = [0, 0, 0]
radius = 8
biggest_triang_int(points_list, sphere_center, radius) == [165, 33.645207682521445, [[[1, 2, -4], [3, 2, 6], [-1, -4, 0]], [[1, 4, 0], [-1, -2, 4], [-3, -2, -6]]]]

Now there are a total of 165 triangles with their vertices in the sphere, the biggest triangle has an area of 33.645207682521445 but we have two triangles with this area value. The vertices of each triangle respect the order of the points list as we expressed before but the additional detail is that the triangles are sorted by the values of the coordinates of their points. Let's compare the coordinates of the first point

First point   x  y  z
Triangle1     1  2 -4  <--- this triangle is first in the result
Triangle2     1  4  0
              |  |
              |  y1 < y2 (2, 4)
              |
              x1 = x2     (1 = 1)

In the case that all the given points are exterior to the sphere the function should output the empty list.

The points in the list are all valid and each one occurs once.

Remember that if three points are collinear do not form a triangle. For practical purposes you may consider that if the area of a triangle is lower than 10-8, the points are aligned.

Enjoy it!
'''
##########################################################################
# input: 球（圆心O坐标[α, β, γ]，半径），point_list(很多点如A\B\C\D\E，每个点坐标[x,y,z])
# output:组成的三角形个数，最大三角形的面积，最大三角形三个顶点坐标（按point_list顺序）
# 限制条件：三角形的顶点在球内，d < r and |(d - r) / r| >10**-10；如果point_list点全在球外，返回空列表
# point_list点有效，且只出现1次
# 三点共线，不能构成三角形；如果三角形面积小于10**-8，这些点共线
# max(area)-area<10**-8  area的点坐标也需返回，有多个点

# distance of two point
def distance(point1,point2):
	d=((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)**0.5
	return d


# point in sphere	
def interior(point_list,center,radius):
	res=[]
	for each in point_list:
		d=distance(each,center)
		if d<radius and (radius-d)/radius>10**-10:
			res.append(each)
	return res 

	
# triangle's area
def area_triangle(A,B,C):
	a=distance(B,C)
	b=distance(A,C)
	c=distance(A,B)
	s=(a+b+c)/2
	area=(s*(s-a)*(s-b)*(s-c))**0.5
	if area>10**-8:
		return area
	else:
		return None


# all available triangle and it's area		
def all_triangle_and_area(interior):
	triangles=[]
	areas=[]
	n=len(interior)
	i=0
	while i<n-2:
		j=i+1
		while j<n-1:
			k=j+1
			while k<n:
				area=area_triangle(interior[i],interior[j],interior[k])
				if area:
					triangles.append([interior[i],interior[j],interior[k]])
					areas.append(area)
				k+=1
			j+=1
		i+=1
	return [triangles,areas]
	

# max triangle area and triangle's three angle
def max_triangle(triangle,area):
	n=len(area)
	biggest_area=max(area)
	biggest_tri=[]
	
	index=0
	while index<n:
		if biggest_area-area[index]<=10**-8:
			biggest_tri.append(triangle[index])
		index+=1
	if len(biggest_tri)==1:
		biggest_tri=biggest_tri[0]
	return [n,biggest_area,biggest_tri]
	
def biggest_triang_int(point_list, center, radius):
	inter=interior(point_list,center,radius)
	triangle_and_area=all_triangle_and_area(inter)
	triangle,area=triangle_and_area
	if (not inter) or (not area):
		return []
	res=max_triangle(triangle,area)
	return res
		
##########################################################################
# TEST CASE		PASSED ALL THE CASES   --> SO HAPPY
'''
points_list1 = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
sphere_center1 = [1, 2, -2]
radius1 = 8
print(biggest_triang_int(points_list1,sphere_center1,radius1))
# result = [4, 22.627416997969508, [[1, 2, -4], [2, 3, 5], [-2, -1, 1]]]
'''

points_list2 = [[1,2,-4],[-3, 2, 4],[7, 8, -4],
[2, 3, 5],[-2, -1, 1],[3, 2, 6],[1, 4, 0], 
[-4, -5, -6],[4, 5, 6],[-2, -3, -5],[-1, -2, 4],
[-3, -2, -6], [-1, -4, 0], [2, 1, -1]]
sphere_center2 = [0, 0, 0]
radius2 = 8
print(biggest_triang_int(points_list2,sphere_center2,radius2))
res = biggest_triang_int(points_list2, sphere_center2, radius2)
# result = [165, 33.645207682521445, [[[1, 2, -4], [3, 2, 6], [-1, -4, 0]], [[1, 4, 0], [-1, -2, 4], [-3, -2, -6]]]]


'''

points_list1 = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
sphere_center1 = [1, 2, -2]
radius1 = 8
res = biggest_triang_int(points_list1, sphere_center1, radius1)
result = [4, 22.627416997969508, [[1, 2, -4], [2, 3, 5], [-2, -1, 1]]]
test.assert_equals(res[0], result[0])
test.assert_equals(res[2], result[2])
assertFuzzyEquals(res[1], result[1])

test.assert_equals(res[0], result[0])
test.assert_equals(res[2], result[2])
assertFuzzyEquals(res[1], result[1])
'''