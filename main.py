from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
POS_X_BORDER = 345
POS_Y_BORDER = 345
NEG_X_BORDER = -345
NEG_Y_BORDER = -345

screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.tracer(0)

scoreboard = ScoreBoard()
snake = Snake()
foods = [Food() for i in range(0,7)] # Create list of foods

screen.listen()
screen.onkey(snake.forwards, "w")
screen.onkey(snake.forwards, "Up")
screen.onkey(snake.backwards, "s")
screen.onkey(snake.backwards, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

screen.title("Snake Game")

game_running = True
while game_running:
        screen.update()
        time.sleep(0.07)
        snake.move_snake()
        
        for food in foods:          #food (adds score for food)
                  if snake.head.distance(food) < 18:
                        scoreboard.update_scoreboard()                
                        food.reset_food()
                        snake.add_snake()       

        #wall collission   
        if snake.head.xcor() > POS_X_BORDER or snake.head.xcor() < NEG_X_BORDER or snake.head.ycor() > POS_Y_BORDER or snake.head.ycor() < NEG_Y_BORDER:
                game_running = False
                scoreboard.game_over()

        #self collission
        for seg in snake.turtles:
                if seg == snake.turtles[0]:
                        pass
                elif snake.head.distance(seg) < 10:
                        game_running = False
                        scoreboard.game_over()

screen.exitonclick()


