from turtle import Turtle, Screen
import time
from paddle import Paddle
from score import Score
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detecting the collosion with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 \
            and ball.xcor() < -325:
        ball.bounce_x()

    # Detect Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()