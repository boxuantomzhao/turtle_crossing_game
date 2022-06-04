import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#------------------------------------- Creating objects
# creating turtles
player = Player()
car_manager = CarManager(fleet_size=10, v_initial=1)

# ------------------------------------ Listen to key inputs
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
i = 0
while game_is_on:
    i += 1
    time.sleep(0.01)
    screen.update()
    car_manager.move()

    if i == 500: # testing only, let the loop run for 5 sec
        game_is_on =  False
        player.write(arg="Done", align="right", font=("arial",20,"normal"))

screen.exitonclick()