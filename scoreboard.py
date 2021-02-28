from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.highscore = 0
        self.goto(-200, 250)
        with open("turtle_scores.txt", 'r') as data:
            self.highscore = int(data.read())

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("turtle_scores.txt", 'w') as data:
                data.write(f"{self.highscore}")

