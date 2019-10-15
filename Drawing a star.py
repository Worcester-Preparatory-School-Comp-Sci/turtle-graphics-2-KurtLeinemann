import turtle

background=turtle.Turtle()
background.color("red")
background.setposition(0,0)
background.pensize(1000)
background.forward(200)
star=turtle.Turtle()
turtle.hideturtle()

star.fillcolor("yellow")
star.begin_fill()
for i in range(0,5):
	star.color(200,1500,0)
	star.pensize(20)
	star.left(72)
	star.forward(70)
	star.right(144)
	star.forward(70)
star.end_fill()
	



	
	
