import turtle as t

FONT = ("Courier", 24, "normal")

# Keep track of the level we are on. If game restarts, the level goes back to 1
class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level {self.level}", False, "center", FONT)
