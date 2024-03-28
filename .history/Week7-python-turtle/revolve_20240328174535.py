from turtle import Turtle, Screen

""" Simulate motion of Mercury, Venus, Earth, and Mars """

planets = {"earth": {"diameter": 1.0, "orbit": 150, "speed": 2, "color": "blue"}}


def revolve(planets):
    # Create a Turtle object for the planet
    earth_turtle = Turtle(shape="circle")
    earth_turtle.color(planets["earth"]["color"])

    # Move the turtle to the starting position
    earth_turtle.penup()
    earth_turtle.sety(-planets["earth"]["orbit"])
    earth_turtle.pendown()

    # Simulate motion of the planet
    earth_turtle.speed("fastest")  # Set speed of the turtle
    earth_turtle.circle(
        planets["earth"]["orbit"], planets["earth"]["speed"]
    )  # Set orbit and speed

    # Keep the window open
    Screen().exitonclick()


# Call the revolve function with the planets dictionary

screen = Screen()
revolve(planets)
screen.exitonclick()
