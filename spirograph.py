import random
from turtle import Turtle, Screen


class Spirograph:
    START_Y = 0
    START_X = 0
    START_HEADING = 0.0
    X_SCREEN_SIZE = 640
    Y_SCREEN_SIZE = 480
    SPEED_FASTEST = 0

    def __init__(self):
        self.walker = Turtle()
        self.walker.shape("classic")
        self.walker.speed(self.SPEED_FASTEST)
        self.walker.pensize(4)
        self.screen = Screen()
        # self.screen.mode("standard")
        self.screen.setup(self.X_SCREEN_SIZE + 30, self.Y_SCREEN_SIZE + 30, self.START_X, self.START_Y)
        self.screen.colormode(255)
        # self.screen.exitonclick()

    def at_starting_position(self):
        position = self.walker.pos()
        return self.START_X - 1 < position[0] < self.START_X + 1 \
            and self.START_Y - 1 < position[1] < self.START_Y + 1 \
            and (self.walker.heading() == self.START_HEADING)

    def draw_random(self):
        if self.on_screen():
            self.set_random_colour()
            self.draw_random_line_length()
            self.turn_random_right_angle()
        else:
            self.snap_back_to_edge()

    def set_random_colour(self):
        colour_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.walker.pencolor(colour_tuple)

    def draw_random_line_length(self):
        self.walker.pendown()
        self.walker.forward(random.randint(0, 50))

    def turn_random_right_angle(self):
        random_right_angle = random.randint(0, 3) * 90
        self.walker.setheading(random_right_angle)

    def turn_heading_by(self, degrees_to_turn: int):
        heading = self.walker.heading()
        self.walker.setheading(heading + degrees_to_turn)

    def on_screen(self) -> bool:
        position = self.walker.pos()
        if abs(position[0]) > self.X_SCREEN_SIZE / 2 or abs(position[1]) > self.Y_SCREEN_SIZE / 2:
            print(f"{position=}")
            return False
        else:
            return True

    def snap_back_to_edge(self):
        # snap position to edge of screen and go randomly from here
        if self.walker.xcor() > self.X_SCREEN_SIZE / 2:
            self.walker.setx(self.X_SCREEN_SIZE / 2)
        if self.walker.xcor() < -self.X_SCREEN_SIZE / 2:
            self.walker.setx(-self.X_SCREEN_SIZE / 2)
        if self.walker.ycor() > self.Y_SCREEN_SIZE / 2:
            self.walker.sety(self.Y_SCREEN_SIZE / 2)
        if self.walker.ycor() < -self.Y_SCREEN_SIZE / 2:
            self.walker.sety(-self.Y_SCREEN_SIZE / 2)

    def draw_circle(self, radius: int):
        self.walker.circle(radius)


my_spiro = Spirograph()
my_spiro.draw_circle(100)
my_spiro.turn_heading_by(10)
while not(my_spiro.at_starting_position()):
    my_spiro.set_random_colour()
    my_spiro.draw_circle(100)
    my_spiro.turn_heading_by(10)

my_spiro.screen.exitonclick()
