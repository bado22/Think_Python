from swampy.TurtleWorld import *

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, ne-1)
	lt(t, angle)
	bk(t, length*n)

Bob = Turtle()	
draw(Bob, 10, 5)