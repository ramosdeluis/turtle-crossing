from turtle import Screen


from player import Player
from board import Board
from cars import Car


CAR_NUMBER = 11


screen = Screen()
screen.tracer(0)
screen.listen()

screen.screensize(600, 600)

player = Player()
cars = []
board = Board()

for number in range(CAR_NUMBER):
    car = Car(number)
    cars.append(car)

screen.onkey(player.move, 'space')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_right, 'd')

is_game_on = True

while is_game_on:
    if board.score == 5:
        board.end_game()
        screen.update()
        is_game_on = False
    # Creating and moving the cars.
    for car in cars:
        car.reset_car()
        car.move()

        # Detect collision.
        if car.distance(player.position()) < 20:
            player.reset_player()
            board.score = 0

    # Making point.
    if player.ycor() > 380:
        board.make_point()
        player.reset_player()

        for car in cars:
            car.speed *= 1.1
    screen.update()

screen.exitonclick()
