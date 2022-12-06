from random import choice, randint
from turtle import Turtle
from time import sleep


class Car(Turtle):
    def __init__(self, car_number):
        super(Car, self).__init__()
        self.shape('square')
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=randint(3, 6))
        self.penup()
        self.sety(-310 + 60 * car_number)
        self.setx(randint(380, 700))
        self.speed = randint(1, 10)/1000
        self.select_color()

    def move(self) -> None:
        sleep(self.speed)
        self.forward(randint(30, 60))

    def select_color(self):
        self.color(choice(['red', 'green', 'yellow', 'black', 'orange']))

    def reset_car(self) -> None:
        if self.xcor() < - 420:
            self.goto(randint(380, 430), self.ycor())
            self.select_color()
