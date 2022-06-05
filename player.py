from turtle import Turtle
STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, move_speed):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)
        self.move_speed = move_speed

    def move_up(self):
        self.forward(self.move_speed)

    def move_down(self):
        self.backward(self.move_speed)