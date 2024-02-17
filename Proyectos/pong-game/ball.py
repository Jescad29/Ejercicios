from turtle import Turtle
from random import randint
import time

ANGLE = randint(1, 360)


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0.1

    def move_random(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.speed_ball *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.speed_ball = 0.1
        self.bounce_x()


