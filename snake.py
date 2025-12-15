from turtle import Turtle
STARTING_POSITIONS = [0,-20,-40]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.head.setheading(0)
        self.head.color("GreenYellow")
    
    def create_snake(self):
        for position in range(0,3):
            segment = Turtle()
            segment.shape("square")
            segment.goto(x=STARTING_POSITIONS[position],y=0)
            segment.penup()
            self.turtles.append(segment)
            segment.color("green2")

    def move_snake(self):
        for turtle in range(len(self.turtles)-1,0,-1): # looping backwards in the lists squares/segments created or added
                self.turtles[turtle].goto(self.turtles[turtle-1].pos()) # moving last square to position of second last square and so on 
                 
        self.head.forward(20)

    def add_snake(self):
        added_snake = Turtle("square")
        added_snake.goto(self.turtles[len(self.turtles)-1].pos())
        added_snake.penup()
        self.turtles.append(added_snake)
        added_snake.color("green2")
        
    def forwards(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def backwards(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

    def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

    def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)