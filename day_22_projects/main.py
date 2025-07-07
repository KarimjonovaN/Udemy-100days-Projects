from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_puddle = Paddle((350, 0))
l_puddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_puddle.go_up,"Up")
screen.onkey(r_puddle.go_down, "Down")
screen.onkey(l_puddle.go_up, "w")
screen.onkey(l_puddle.go_down, "s")



game_is_on= True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #detect collision with the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_puddle) < 50 and ball.xcor() > 320 or ball.distance(l_puddle) < 50 and ball.xcor() < -320:
        print(f"{ball.xcor()}  {ball.ycor()} ")
        print(f"{r_puddle.xcor()} {r_puddle.ycor()}")
        print(f"{l_puddle.xcor()} {l_puddle.ycor()}")
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()