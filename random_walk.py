import random
from random import choice
from turtle import Turtle, Screen


class RandomWalker:
    START_Y = 0
    START_X = 0
    Y_SCREEN_SIZE = 768
    X_SCREEN_SIZE = 1024
    SPEED_FASTEST = 0

    def __init__(self):
        self.walker = Turtle()
        # self.walker.shape("classic")
        self.walker.hideturtle()
        self.walker.speed(self.SPEED_FASTEST)
        self.walker.pensize(8)
        self.screen = Screen()
        self.screen.setup(self.X_SCREEN_SIZE, self.Y_SCREEN_SIZE,
                          self.START_X, self.START_Y)
        self.screen.colormode(255)
        # self.my_screen.exitonclick()

    def walk(self):
        if self.on_screen():
            self.set_random_colour()
            self.draw_random_line_length()
            self.turn_random_right_angle()
        else:
            # snap position to edge of screen and go randomly from here
            if self.walker.xcor() > self.X_SCREEN_SIZE / 2:
                self.walker.setx(self.X_SCREEN_SIZE / 2)
            if self.walker.xcor() < -self.X_SCREEN_SIZE / 2:
                self.walker.setx(-self.X_SCREEN_SIZE / 2)
            if self.walker.ycor() > self.Y_SCREEN_SIZE / 2:
                self.walker.sety(self.Y_SCREEN_SIZE / 2)
            if self.walker.ycor() < -self.Y_SCREEN_SIZE / 2:
                self.walker.sety(-self.Y_SCREEN_SIZE / 2)

    def set_random_colour(self):
        colour_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.walker.pencolor(colour_tuple)

    def draw_random_line_length(self):
        self.walker.pendown()
        # self.walker.forward(30)
        self.walker.forward(random.randint(0, 50))

    def turn_random_right_angle(self):
        random_right_angle = random.randint(0, 3) * 90
        self.walker.setheading(random_right_angle)

    def on_screen(self):
        position = self.walker.pos()
        if abs(position[0]) > self.X_SCREEN_SIZE / 2 or \
           abs(position[1]) > self.Y_SCREEN_SIZE / 2:
            print(f"{position=}")
            return False
        else:
            return True


walker = RandomWalker()
while 1:
    walker.walk()

