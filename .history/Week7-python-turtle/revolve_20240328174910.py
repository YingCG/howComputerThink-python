from turtle import Turtle, Screen
import math

# Create a dictionary to store planet data
planets = {"earth": {"diameter": 1.0, "orbit": 150, "speed": 2, "color": "blue"}}


def revolve(planets):
    # Create a Turtle object for the planet
    earth_turtle = Turtle(shape="circle")
    earth_turtle.color(planets["earth"]["color"])

    # Move the turtle to the starting position
    earth_turtle.penup()
    earth_turtle.sety(-planets["earth"]["orbit"])
    earth_turtle.pendown()

    # Hide the turtle's pen
    earth_turtle.penup()

    # Simulate motion of the planet
    angle = 0
    while True:
        # Calculate the new position using trigonometry
        x = planets["earth"]["orbit"] * math.cos(math.radians(angle))
        y = planets["earth"]["orbit"] * math.sin(math.radians(angle))

        # Move the turtle to the new position
        earth_turtle.goto(x, y)

        # Show the turtle's pen
        earth_turtle.pendown()

        # Increment the angle based on the speed
        angle += planets["earth"]["speed"]

        # Wrap the angle around if it exceeds 360 degrees
        angle %= 360

        # Hide the turtle's pen again for next iteration
        earth_turtle.penup()


# Create the screen
screen = Screen()

# Call the revolve function with the planets dictionary
revolve(planets)

# Keep the window open
screen.exitonclick()
