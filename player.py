from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setpos(0, -280)
        self.showturtle()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.setheading(90)

    # def move(self):
    #     new_x = self.xcor() + self.x_move
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x, new_y)
    #
    def move_up(self):
        self.setheading(90)
        new_x = self.xcor()
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def move_left(self):
        self.setheading(180)
        new_x = self.xcor() - MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)
    def move_right(self):
        self.setheading(0)
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)
    def move_down(self):
        self.setheading(270)
        new_x = self.xcor()
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(new_x, new_y)
    def reset(self):
        self.hideturtle()
        self.setpos(0, -280)
        self.setheading(90)
        self.showturtle()

    # def bounce(self):
    #     self.y_move *= -1
    #
    # def collision(self):
    #     self.x_move *= -1
    #
    # def reset(self):
    #     self.hideturtle()
    #     self.setpos(0, 0)
    #     self.showturtle()
    #     self.x_move *= -1
