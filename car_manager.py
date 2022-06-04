from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5



class CarManager(Turtle):
    def __init__(self, fleet_size, v_initial):
        super().__init__()
        self.hideturtle()
        self.fleet_size = fleet_size # num of cars on screen
        self.fleet = [] # List of all the car objects
        self.fleet_v = v_initial
        for i in range(self.fleet_size):
            self.generate_car(position=(random.randint(-290,290),random.randint(-290,290)))

    def generate_car(self,position):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2) # 20x40 cars to begin with
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.initial_pos = (position)
        new_car.setposition(new_car.initial_pos)
        self.fleet.append(new_car)

    def move(self):
        for car in self.fleet:
            car.forward(self.fleet_v)

    def replenish(self):
        for car in self.fleet:
            if car.xcor() < -290:
                #one car has left the screen, reset it back to the right side
                #change the color/size/position so that it looks like a new car


