from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.all_snakes.append(new_segment)

    def extending_snakes(self):
        self.add_segments(self.all_snakes[-1].position())

    def move(self):
        for num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[num - 1].xcor()
            new_y = self.all_snakes[num - 1].ycor()
            self.all_snakes[num].goto(new_x, new_y)
        self.head.forward(20)

    def reset(self):

        for key in self.all_snakes:
            key.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

    def up(self):

        if self.head.heading() != DOWN:
            self.all_snakes[0].setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
