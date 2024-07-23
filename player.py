import turtle as t
from constants import HEADING_VALUES

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(HEADING_VALUES["up"])

    def detect_car_collision(self):
        # get all turtles on screen and see if turtle has made contact with one of them
        pass

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.setpos(STARTING_POSITION)
