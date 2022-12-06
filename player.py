from turtle import Turtle
from time import sleep


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.sety(-348)
        self.speed = 0.18
        self.color('blue')

    def move(self):
        sleep(self.speed)
        self.forward(30)

    def move_right(self):
        new_x = self.xcor() + 25
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 25
        self.goto(new_x, self.ycor())

    def reset_player(self):
        self.setposition(0, -348)
