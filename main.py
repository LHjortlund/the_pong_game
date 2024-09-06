from turtle import Turtle, Screen
UP = 90
DOWN = 270

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)




paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def paddle_up():
    new_y= paddle.ycor()+20
    paddle.goto(paddle.xcor(), new_y)

def paddle_down():
    new_y= paddle.ycor()-20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()