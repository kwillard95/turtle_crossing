import turtle as t
import random as r
from constants import HEADING_VALUES

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_CREATION_START_X_POINT = 315


class CarManager:
    def __init__(self, screen):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE
        screen.ontimer(self.create_car, 1000)

    def create_car(self):
        random_chance = r.randint(1, 6)
        if random_chance == 6:
            car = t.Turtle()
            car.color(r.choice(COLORS))
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.setheading(HEADING_VALUES["left"])
            car.setpos((r.randint(315, 315 * 2), r.randint(-280, 280)))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.current_speed)

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT
