import math

def circle_area(xc, yc, xp, yp):
	dx = xp - xc
	dy = yp - yc
	radius = math.sqrt(dx**2 + dy**2)
	area = math.pi * radius**2
	print area
	return area
	
circle_area(0,0, 10, 10)