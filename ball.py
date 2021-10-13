from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.speed(1)


    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)



    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def restart(self):
        self.speed(0)
        self.setposition(0, 0)
        self.speed(1)
        self.bounce_x()


