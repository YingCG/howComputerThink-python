class Cat:
    name: None
    age: None
    __isHappy: None

    # constructor
    def __init__(self, name, age, isHappy=True):
        self.name = (name,)
        self.age = (age,)
        self.__isHappy = isHappy

    def sound(self):
        print("Meow~")

    def display(self):
        print("****CAT***")
        print("name: ", self.name)
        print("age: ", self.age)
        print("happy: ", self.__isHappy)

    # getter
    def get_isHappy(self):
        return self.__isHappy

    # setter
    def set_isHappy(self, new_happy):
        self.__isHappy = new_happy


# child class
class DometicCat(Cat):
    owner: None

    def __init__(self, owner, name, age, isHappy=True):
        super().__init__(name, age, isHappy)
        self.owner = owner


class WildCat(Cat):
    def sound(self):
        print("Hiss")


# create instance
cat1 = Cat("Mao Mao", 3)
print(cat1.sound())

cat2 = DometicCat("Mikhir", "KitKat", 2)
print(cat2.owner)
