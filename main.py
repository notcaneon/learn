from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()


screen.bgcolor("black")
screen.setup(width=700,height=700)

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.forwards, "w")
screen.onkey(snake.forwards, "Up")
screen.onkey(snake.backwards, "s")
screen.onkey(snake.backwards, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")


game_running = True
while game_running:
        screen.update()
        time.sleep(0.09)
        snake.move_snake()
        
        if snake.head.distance(food) < 18:
                scoreboard.update_scoreboard()                
                food.reset_food()
                snake.add_snake()


screen.title("Snake Game")

screen.exitonclick()
