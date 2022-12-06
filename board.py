from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super(Board, self).__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-400, 340)
        self.score = 0
        self.write_board()

    def write_board(self):
        self.clear()
        self.write(f'Score: {self.score}/5', move=False, align='left', font=('Arial', 32, 'normal'))

    def make_point(self):
        self.score += 1
        self.write_board()

    def end_game(self):
        self.home()
        self.clear()
        self.write(f'Congratulations! You win the game.', move=False, align='center', font=('Arial', 32, 'normal'))