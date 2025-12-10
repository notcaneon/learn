from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(-27,315) 
        self.write(arg=f"Score:{self.score} ",move=False,align = "left",font=("Arial", 24, "normal"))
        
    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score} ",move=False,align = "left",font=("Arial", 24, "normal"))