import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard





screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

player = Player()
scoreboard = Scoreboard()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_down, "s")
screen.onkeypress(player.move_right, "d")



manager = CarManager()
manager.create_cars()
x_checker = 0

CAR_SPEED = 0.1

game_is_on = True
while game_is_on:
    time.sleep(CAR_SPEED)
    screen.update()
    scoreboard.write(f"Score: {scoreboard.score} High Score: {scoreboard.highscore}", False, "Left", ("Courier", 24, "normal"))

    for i in range(0, len(manager.car_list)):
        manager.car_list[i].move()
        if player.distance(manager.car_list[i]) < 30:
            scoreboard.score = 0
            scoreboard.clear()
            player.reset()
    if manager.car_list[x_checker].xcor() < 230:
        manager.create_cars()
        x_checker += manager.CARS_PER_WAVE
    if player.ycor() > 280:
        player.reset()
        scoreboard.clear()
        scoreboard.increase_score()
        CAR_SPEED *= 0.9








file.close()
screen.exitonclick()