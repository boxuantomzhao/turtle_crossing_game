import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.textinput(title="Welcome to turtle crossing",prompt="Help the turtle cross the street, move with w-s key,"
                                                           " press ok to start")
difficulty = screen.numinput(title="Choose difficulty level", prompt="type in 1 for easiest, 4 for hardest")

#------------------------------------- Creating objects
# creating turtles
player = Player(move_speed=20) #num of pixels moved per key press

num_cars = int(difficulty*10) #num of cars on screen
car_manager = CarManager(fleet_size=num_cars, v_initial=2)

scoreboard = Scoreboard()

# ------------------------------------ Listen to key inputs
screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

game_is_on = True
i = 0
while game_is_on:
    i += 1
    time.sleep(0.01)
    screen.update()
    car_manager.move()
    car_manager.replenish()
    scoreboard.show_score()

    # If player reached the top - > next level
    if player.ycor() > 290:
        player.setposition(0,-280)
        car_manager.level_up() #car speed increase
        scoreboard.add_level()

    # Collision detection
    for car in car_manager.fleet:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()