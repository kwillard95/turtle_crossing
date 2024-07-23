import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


turtle = Player()
car_manager = CarManager(screen)


def start_game():

    def run_game():
        car_manager.create_car()
        if turtle.is_at_finish_line():
            turtle.reset_player()
        else:
            car_manager.move_cars()
        time.sleep(0.1)
        screen.update()
        run_game()

    screen.onkeypress(turtle.move_player, "Up")
    run_game()


start_game()
screen.exitonclick()




