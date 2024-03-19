class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def legs(self):
        return self._legs

    def speak(self):
        return self.name + "say: Bark!"


# create instance
myDog = Dog("Rover")
print(myDog.name)
print(myDog.legs())
print(myDog.speak())
