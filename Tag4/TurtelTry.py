import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle named 'spiral'
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest drawing speed

# Define a list of colors
colors = ["red", "green", "blue", "yellow", "orange", "purple", "white", "cyan"]

# Function to draw a spiral
def draw_spiral(turtle, turn_angle, max_len, color_change_step):
    length = 1
    while length < max_len:
        turtle.forward(length)
        turtle.right(turn_angle)
        length += 1
        if length % color_change_step == 0:
            turtle.color(random.choice(colors))

# Draw the spiral
spiral.penup()
spiral.goto(0, 0)  # Start at the center of the screen
spiral.pendown()
draw_spiral(spiral, 91, 400, 20)  # Adjust parameters to change the pattern

# Hide the turtle and finish
spiral.hideturtle()
turtle.done()

