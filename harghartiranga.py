#Indian National Flag using turtle
import turtle

t = turtle.Pen()

#setting screen size to maximum
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

#background color
turtle.bgcolor('light cyan')

#setting turtle
t.speed(12000)
t.hideturtle()
t.color('white')
t.setx(-500)
t.sety(100)
t.color('black')

#orange band
t.color('dark orange')
t.fillcolor('dark orange')
t.begin_fill()
t.forward(250*4)
t.left(90)
t.forward(70*3) 
t.left(90)  
t.forward(250*4) 
t.left(90) 
t.forward(70*3) 
t.end_fill()

#white band
t.color('white')
t.fillcolor('white')
t.begin_fill()
t.forward(70*3)
t.left(90)
t.forward(250*4)
t.left(90)
t.forward(70*3)
t.left(90)
t.forward(250*4)
t.left(90)
t.forward(70*3)
t.end_fill()

#green band
t.color('green')
t.fillcolor('green')
t.begin_fill()
t.forward(70*3)
t.left(90)
t.forward(250*4)
t.left(90)
t.forward(70*3)
t.left(90)
t.forward(125*4)
t.end_fill()

#center to ashok chakra
t.width(10)
t.color('blue')
t.right(180)
t.circle(35*3)
t.width(0.2)
t.color('white')
t.backward(4*4)

#spokes of ashok chakra
t.color('blue')
t.width(10)
t.left(90)
t.fillcolor('blue')
t.begin_fill()
for i in range(48):
	t.forward(69*3)
	t.left(90)
	t.left(15)
	t.left(90)
t.forward(70*3)
t.end_fill()
t.down()

#Happy 75th Independence day
t.color('red')
t.up()
t.hideturtle()
t.setx(379)
t.sety(-390)
t.write("Happy 75th Independence day !",move=True, align="right",font=('Courier','32','bold'))
t.down()

#Azadi Ka Amrit Mahotsav
t.up()
t.hideturtle()
t.setx(270)
t.sety(330)
t.write("#azadikaamritmahotsav",move=True, align="right",font=('Courier','32','bold'))

turtle.exitonclick()
