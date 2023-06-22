from turtle import Turtle

# Declare as CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
            for seg_num in range(len(self.segments) - 1, 0, -1):
            # for seg_num in range(start=len(segments) - 1, stop=0, step=-1):
            # for seg_num in range(start=2, stop=0, step=-1):
                new_y = self.segments[seg_num - 1].ycor()
                new_x = self.segments[seg_num - 1].xcor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            #  move North / 90 deg
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            # move South / 270 def
            self.head.setheading(DOWN)
         
    def left(self):
        if self.head.heading() != RIGHT:
            #  move West / 180 deg
            self.head.setheading(LEFT)
         
    def right(self):
        if self.head.heading() != LEFT:
            #  move East / 0 deg
            self.head.setheading(RIGHT)