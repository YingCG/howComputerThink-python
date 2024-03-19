class Character():
    name: None
    health_points: None
    mana_points: None

    # constructor
    def __init__(self, p_name):
        self.name = p_name
        self.health_points = 100

    # display
    def display(self):
        if self.health_points >= 50:
            print("0_0")
        elif self.health_points > 0:
            print("O_o")
        else:
            print("x_x")

    # damage function
    # parameter: the number of damage points
    def damage(self, points):
        self.health_points -= points

        if self.health_points < 0:
            self.health_points = 0

    def heal(self, points):
        self.health_points += points

        if self.health_points > 100:
            self.health_points = 100

Geralt = Character("Geralt")
# Geralt.name = "Geralt"
# Geralt.health_points = 100

Geralt.display()
Geralt.damage(80)
Geralt.display()
Geralt.damage(80)
Geralt.display()
Geralt.heal(1000)
Geralt.display()

Ciri = Character("Ciri")
Ciri.display()

