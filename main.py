from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball
from scoreboard import ScoreBoard
import time

main_screen = Screen()
main_screen.bgcolor('black')
main_screen.setup(height=600, width=800)
main_screen.title("PONG")
middle_line = Turtle()
middle_line.color("white")
middle_line.shape("square")
middle_line.left(90)
middle_line.shape("square")
for x in range(0, 380, 20):
    middle_line.penup()
    middle_line.dot(size=7)
    middle_line.goto(x=0, y=x)

for x in range(0, 380, 20):
    middle_line.penup()
    middle_line.dot(size=7)
    middle_line.goto(x=0, y=-1 * x)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreBoard = ScoreBoard()

main_screen.listen()
main_screen.onkey(r_paddle.go_up, 'Up')
main_screen.onkey(r_paddle.go_down, 'Down')

main_screen.onkey(l_paddle.go_up, 'w')
main_screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() >= 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        print("Made Contact")
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.restart()
        scoreBoard.l_point()
        scoreBoard.updateScoreBoard()
    if ball.xcor() < -350:
        ball.restart()
        scoreBoard.r_point()
        scoreBoard.updateScoreBoard()
main_screen.exitonclick()
