from turtle import Turtle, Screen

""" Simulate motion of Mercury, Venus, Earth, and Mars """

planets = {"earth": {"diameter": 1.0, "orbit": 150, "speed": 2, "color": "blue"}}


def revolve():
    for planet in planets:
        dictionary = planets[planet]
        dictionary["turtle"].circle(dictionary["orbit"], dictionary["speed"])


screen = Screen()

revolve(planets)

screen.exitonclick()
