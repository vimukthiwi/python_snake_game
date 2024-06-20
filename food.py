from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize the food to be smaller
        self.color("green")  # Set the color of the food to green
        self.speed("fastest")  # Set the speed of the turtle to the fastest
        self.refresh()  # Place the food at a random location

    def refresh(self):
        """Move the food to a new random location on the screen."""
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new location
