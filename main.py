import time
from turtle import Turtle, Screen
from snake import Snake, STARTING_POSITIONS
from food import Food
from scoreboard import Scoreboard

screen = Screen()
wall = screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("my snake game ")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

on = True
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.food_random()
        snake.extending_snakes()
        score_board.counter_of_food()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        score_board.high_score_func()
        snake.reset()
    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.high_score_func()
        snake.reset()
    for key in snake.all_snakes[1:]:
        if snake.head.distance(key) < 10:
            score_board.high_score_func()
            snake.reset()

screen.exitonclick()
