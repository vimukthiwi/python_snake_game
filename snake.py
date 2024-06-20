from turtle import Turtle
import time

# Constants for initial snake position and movement
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # List to store snake segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The first segment is the head

    def create_snake(self):
        """Create the initial snake with three segments."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to the snake at the given position."""
        new_segment = Turtle("square")  # Create a new segment
        new_segment.color("white")  # Set the color of the segment
        new_segment.penup()  # Lift the pen to avoid drawing lines
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the segment to the segments list

    def extend(self):
        """Extend the snake by adding a new segment at the position of the last segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by updating the positions of the segments."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the segment to the position of the previous segment
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change the direction of the snake to up if it's not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the direction of the snake to down if it's not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the direction of the snake to left if it's not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the direction of the snake to right if it's not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
