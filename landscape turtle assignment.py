#Kurt Leinemann Landscape 14 October 2019
from turtle import *
skyAndHorizon=Turtle() #draws space and moon horizon
hideturtle()
penup()
goto(-200,-200)
pendown()
fillcolor(0,0,0)
begin_fill()
for i in range(0,4):
	forward(400)
	left(90)
end_fill()
fillcolor("gray")
begin_fill()
left(90)
forward(30)
pencolor("gray")
right(90)
forward(400)
right(90)
forward(30)
right(90)
forward(400)
end_fill()	

def island(x,y,size): #draws the islands on earth as green circles
	penup()
	goto(x,y)
	pencolor("green")
	fillcolor("green")
	pensize(10)
	pendown()
	begin_fill()
	circle(size)
	end_fill()

earth=Turtle() #draws the earth
pencolor("blue")
pensize(120)
fillcolor("blue")
penup()
goto(80,115)
pendown()
circle(50)
island(50,70,10)
island(100,80,20)
island(150,110,5)
island(55,150,20)
island(80,0,15)


def landingLegs(): #draws both landing legs
	penup()
	goto(-130,0)
	pendown()
	pencolor("gray")
	pensize(5)
	right(135)
	forward(20)
	penup()
	left(135)
	goto(-70,0)
	pendown()
	right(45)
	forward(20)
	left(45)
	
spaceship=Turtle()
fillcolor("lightblue") #This draws the cab 
pencolor("lightblue")
pensize(2)
penup()
goto(-100,80)
pendown()
begin_fill()
circle(30)
end_fill()

landingLegs() 

penup()
goto(-110,10) #This draws the base or body of the ship
pendown()
pencolor("white")
fillcolor("white")
begin_fill()
forward(50)
right(135)
forward(30)
right(45)
forward(80)
right(45)
forward(30)
right(135)
forward(50)
end_fill()












