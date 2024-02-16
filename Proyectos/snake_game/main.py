from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

foods = Food()
snakes = Snake()
scoreboard = ScoreBoard()

screen.onkey(snakes.up, "w")
screen.onkey(snakes.down, "s")
screen.onkey(snakes.left, "a")
screen.onkey(snakes.right, "d")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    # Detect collision with food.
    if snakes.head.distance(foods) < 15:
        foods.refresh()
        snakes.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snakes.head.xcor() > 300 or snakes.head.xcor() < -300 or snakes.head.ycor() > 300 or snakes.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for n in snakes.snake[1:]:
        if snakes.head.distance(n) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
