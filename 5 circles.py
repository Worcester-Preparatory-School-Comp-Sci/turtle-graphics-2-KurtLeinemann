import turtle
from random import *
for x in range(1,6):
	turtle.fillcolor("blue")
	turtle.begin_fill()
	turtle.penup()
	turtle.setposition((x*35)-100,(x*35)-100)
	turtle.pendown()
	turtle.color(randint(0,255),randint(0,255),randint(0,255))
	circle=turtle.circle(25)
	turtle.end_fill()
	
