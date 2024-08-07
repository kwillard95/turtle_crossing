import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", False, "center", FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
        self.goto(0, -30)
        self.write(f"You made it to Level {self.level}", False, "center", FONT)
        self.screen.ontimer(self.clear, 5000)
