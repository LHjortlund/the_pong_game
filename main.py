from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))  #Højre paddle
l_paddle = Paddle((-350, 0))  #Venstre paddle
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")        #Flytter højre paddle op
screen.onkey(r_paddle.go_down, "Down")    #Flytter højre paddle ned

screen.onkey(l_paddle.go_up, "w")         #Flytter venstre paddle op
screen.onkey(l_paddle.go_down, "s")       #Flytter venstre paddle ned

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()

screen.exitonclick()