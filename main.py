from turtle import Turtle, Screen
import time
screen = Screen()

turtles = []
screen.bgcolor("black")
screen.setup(width=1000,height=600)
starting_positions = [-20,0,20]
screen.tracer(0)
for position in range(0,3):
        segment = Turtle()
        segment.shape("square")
        segment.goto(x=starting_positions[position],y=0)
        segment.penup()
        turtles.append(segment)
        segment.color("white")

def turn_forwards():
        turtles[0].setheading(90)

def turn_backwards():
        turtles[0].setheading(270)

def turn_left():
        turtles[0].setheading(180)

def turn_right():
        turtles[0].setheading(0)

screen.listen()
screen.onkey(turn_forwards, "w")
screen.onkey(turn_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")



game_running = True
while game_running:
        screen.update()
        for turtle in range(len(turtles)-1,0,-1): 
                turtles[turtle].goto(turtles[turtle-1].pos())
                time.sleep(0.03) 
        turtles[0].forward(20)

screen.title("Snake Game")

screen.exitonclick()
