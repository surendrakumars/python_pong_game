from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle_r.up)
screen.onkey(key="Down", fun=paddle_r.down)

screen.onkey(key="w", fun=paddle_l.up)
screen.onkey(key="s", fun=paddle_l.down)

is_on = True
sleep = 0.2
while is_on:
    time.sleep(sleep)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle

    if ball.distance(paddle_r.paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle_l.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep = sleep*0.9
    if ball.xcor() > 380:
        ball.reset_l()
        score.l_point()
        sleep = 0.1
    if ball.xcor() < -380:
        ball.reset_r()
        score.r_point()
        sleep = 0.1
screen.exitonclick()
