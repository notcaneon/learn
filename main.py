from turtle import Turtle, Screen
screen = Screen()
x_cord = -40
turtles = []
screen.bgcolor("black")
screen.setup(width=1000,height=800)
for turtle in range(1,4):
    turtle = Turtle()
    turtle.shape("square")
    turtle.goto(x=x_cord,y=0)
    x_cord += 20
    turtle.color("white")
    turtles.append(turtle)
    print(x_cord)
screen.exitonclick()
