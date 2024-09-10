from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))  #Højre paddle
l_paddle = Paddle((-350, 0))  #Venstre paddle
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")        #Flytter højre paddle op
screen.onkeypress(r_paddle.go_down, "Down")    #Flytter højre paddle ned

screen.onkeypress(l_paddle.go_up, "w")         #Flytter venstre paddle op
screen.onkeypress(l_paddle.go_down, "s")       #Flytter venstre paddle ned

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect if l_paddle misses
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()