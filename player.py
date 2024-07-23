import turtle as t
from constants import HEADING_VALUES

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(HEADING_VALUES["up"])

    def detect_car_collision(self, cars):
        for car in cars:
            if self.distance(car) <= 10:
                return True
        return False

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.setpos(STARTING_POSITION)
