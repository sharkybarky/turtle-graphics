import random
from turtle import Turtle, Screen
import colorgram

DOT_SIZE = 15
DOT_SPACING = 25
NUM_DOTS_X = 10
NUM_DOTS_Y = 20
X_SCREEN_SIZE = (NUM_DOTS_X * DOT_SPACING) + DOT_SIZE
Y_SCREEN_SIZE = (NUM_DOTS_Y * DOT_SPACING) + DOT_SIZE
START_DRAW_X = -X_SCREEN_SIZE / 2
START_DRAW_Y = Y_SCREEN_SIZE / 2

drawer = Turtle()
screen = Screen()
drawer.speed(0)
drawer.hideturtle()
screen.setup(X_SCREEN_SIZE + 40, Y_SCREEN_SIZE + 40, 0, 0)
screen.colormode(255)
colours = colorgram.extract("./resources/download.jpg", 100)


def move_pen_to(x_coord, y_coord):
    drawer.penup()
    drawer.goto(x_coord, y_coord)
    drawer.pendown()


move_pen_to(START_DRAW_X, START_DRAW_Y)
for _ in range(NUM_DOTS_Y):
    for _ in range(NUM_DOTS_X):
        pos = drawer.pos()
        dot_colour = random.choice(colours)
        drawer.dot(DOT_SIZE, (dot_colour.rgb.r, dot_colour.rgb.g, dot_colour.rgb.b))
        # increment x pos by 10
        move_pen_to(pos[0] + DOT_SPACING, pos[1])
    # move y pos down and set x back to START_DRAW_X
    move_pen_to(START_DRAW_X, pos[1] - DOT_SPACING)

screen.exitonclick()
