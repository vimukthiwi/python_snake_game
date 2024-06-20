import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off screen updates

# Create the snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key listeners for snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause the game for a moment
    snake.move()  # Move the snake

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food location
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score

    # Check for collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()  # End the game

    # Check for collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()  # End the game

# Exit the game when the screen is clicked
screen.exitonclick()
