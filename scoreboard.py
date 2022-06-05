from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def show_score(self):
        self.setposition(-230,260)
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font = FONT)

    def add_level(self):
        self.level += 1

    def game_over(self):
        self.setposition(0,0)
        FONT = ("Courier", 20, "bold")
        self.write(arg=f"Game Over", move=False, align="center", font=FONT)




