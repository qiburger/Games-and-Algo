from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()
print bob

bob.delay = 0.01

def polygon(t, n, length):
	for i in range(n):
		theta = 360.0 / n
		fd(t, length)
		lt(t, theta)

def circle(t, r, n):
	arc_length = 2 * pi * r / n
	polygon(t, n, arc_length)

def arc(t, r, angle):
	n = int(r / 2) + 10
	arc_length = (2 * pi * r * angle / 360.0) / n
	polygon(t, n, arc_length)

arc(bob, r = 2000, angle = 30.0)
