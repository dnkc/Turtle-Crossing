COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.CARS_PER_WAVE = 5
        self.car_list = []
        self.penup()
        self.rand_y = random.randint(-250, 280)
        self.hideturtle()
        self.setpos(320, self.rand_y)
        self.showturtle()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_wid=1, stretch_len=2)

    def move(self):
        new_x = self.xcor() + STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def create_cars(self):
        for j in range(0, self.CARS_PER_WAVE):
            j = CarManager()
            self.car_list.append(j)
