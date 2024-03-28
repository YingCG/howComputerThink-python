from turtle import Turtle, Screen


class Planet:
    def __init__(self, name, diameter, orbit, speed, color):
        self.name = name
        self.diameter = diameter
        self.orbit = orbit
        self.speed = speed
        self.color = color
        self.turtle = Turtle(shape="circle")
        self.setup()

    def setup(self):
        self.turtle.speed("fastest")
        self.turtle.shapesize(self.diameter)
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.sety(-self.orbit)
        self.turtle.pendown()

    def revolve(self):
        self.turtle.circle(self.orbit, self.speed)


planets_data = {
    "mercury": {"diameter": 0.383, "orbit": 58, "speed": 7.5, "color": "gray"},
    "venus": {"diameter": 0.949, "orbit": 108, "speed": 3, "color": "yellow"},
    "earth": {"diameter": 1.0, "orbit": 150, "speed": 2, "color": "blue"},
    "mars": {"diameter": 0.532, "orbit": 228, "speed": 1, "color": "red"},
}


def setup_planets(planets_data):
    planets = {}
    for name, data in planets_data.items():
        planets[name] = Planet(name, **data)
    return planets


def revolve_all(planets):
    for planet in planets.values():
        planet.revolve()
    screen.ontimer(lambda: revolve_all(planets), 50)


screen = Screen()
planets = setup_planets(planets_data)
revolve_all(planets)
screen.exitonclick()
