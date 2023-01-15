from turtle import *
import random

START_Y = 0
START_X = 0
Y_SCREEN_SIZE = 768
X_SCREEN_SIZE = 1024

# setup turtle appearance
timmy = Turtle()
timmy.color("red", "yellow")
timmy.shape("turtle")
timmy.turtlesize(2)  # double size

# setup screen
my_screen = Screen()
my_screen.setup(X_SCREEN_SIZE, Y_SCREEN_SIZE, START_X, START_Y)
MIN_X_POS = -my_screen.canvwidth
MIN_Y_POS = -my_screen.canvheight


def print_pos():
    print(f"{timmy.pos()=}")


# move turtle
timmy.goto(0, 0)
timmy.fd(10)
print_pos()
timmy.goto(200, 200)
timmy.fd(10)
print_pos()
timmy.goto(-200, -200)
timmy.fd(10)
print_pos()
timmy.goto(MIN_X_POS, MIN_X_POS)
timmy.fd(10)
print_pos()
timmy.goto(-X_SCREEN_SIZE/2, -Y_SCREEN_SIZE/2)
timmy.fd(10)
print_pos()
my_screen.exitonclick()

timmy.speed(200)
timmy.begin_fill()
while 1:
    timmy.forward(random.randint(210, 300))
    timmy.rt(170)
    if abs(timmy.pos()) < 1:
        break

    # position =
    if (position := timmy.pos())[0] < MIN_X_POS:
        print(f"{position=}")
        timmy.goto(0, 0)

timmy.end_fill()
my_screen.exitonclick()
