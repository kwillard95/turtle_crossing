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





def start_game():
    turtle = Player()
    car_manager = CarManager(screen)
    scoreboard = Scoreboard()
    restart_game = False
    def run_game():
        car_manager.create_car()
        is_car_collision = turtle.detect_car_collision(car_manager.cars)
        if is_car_collision:
            restart_game = True
        if turtle.is_at_finish_line():
            scoreboard.level += 1
            scoreboard.write_level()
            car_manager.increase_difficulty(scoreboard.level)
            turtle.reset_player()

        else:
            car_manager.move_cars()
        time.sleep(0.1)
        screen.update()
        run_game()
        # if not restart_game:
        #     run_game()
    # if restart_game:
    #     start_game()

    screen.onkeypress(turtle.move_player, "Up")
    run_game()


start_game()
screen.exitonclick()




