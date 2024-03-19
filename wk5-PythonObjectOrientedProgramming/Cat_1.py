from winsound import Beep

# constants for colours
BLUE = "\033[34m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
DEFAULT = "\033[39m"
RESET = "\033[0m"

class Cat:
    name: None
    age: None
    color: None
    color_code: None

    # constructor
    def __init__(self, name, age, color = ""):
        self.name = name
        self.age = age
        self.color = color

        # color code
        if color == "blue":
            self.color_code = BLUE
        elif color == "magenta":
            self.color_code = MAGENTA
        elif color == "green":
            self.color_code = GREEN
        else:
            self.color_code = DEFAULT
            self.color = "default"

    # display data
    def display_info(self):
        print(f"*** cat: {self.name} ***")
        print("age: ", self.age)
        print(f"color: {self.color_code}{self.color}{RESET} ")

    # draw a cat
    def display(self):
        print(f'''{self.color_code}
(\___/)
(=*.*=)  
U-----U
  {RESET}''')

    # "Meow"   
    def sound(self):
        print("Meow!\n")
        Beep(300, 1000)
        Beep(200, 500)
    

