from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.goto(0, 0)
        self.setheading(180)
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(300, 0)
        self.color(choice(COLORS))
        self.move_distance += MOVE_INCREMENT
