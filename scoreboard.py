from turtle import Turtle

# Constants for alignment and font
ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize score
        self.color("White")  # Set color of the scoreboard text
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 260)  # Position the scoreboard at the top of the screen
        self.hideturtle()  # Hide the turtle shape
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        """Display 'Game Over' message in the center of the screen."""
        self.goto(0, 0)  # Move to the center of the screen
        self.write("Game Over!", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1  # Increment the score
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Update the scoreboard with the new score
