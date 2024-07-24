import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def start_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    turtle = Player()
    car_manager = CarManager(screen)
    scoreboard = Scoreboard()
    game_running = True

    def run_game():
        nonlocal game_running
        car_manager.create_car()
        is_car_collision = turtle.detect_car_collision(car_manager.cars)
        should_start_round = car_manager.should_start_round()
        if not should_start_round:
            car_manager.move_cars()
        else:
            screen.onkeypress(turtle.move_player, "Up")
            if is_car_collision:
                game_running = False
            elif turtle.is_at_finish_line():
                scoreboard.increase_level()
                car_manager.increase_difficulty(scoreboard.level)
                turtle.reset_player()
            else:
                car_manager.move_cars()
        time.sleep(0.1)
        screen.update()
        if game_running:
            run_game()
    run_game()
    if not game_running:
        screen.clear()
        scoreboard.game_over()
        screen.ontimer(start_game, 5000)
    screen.exitonclick()


start_game()





