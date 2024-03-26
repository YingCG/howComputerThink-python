"""
Interface to describe objects that can be printed
"""
class IPrintable:
    def print_info(self):
        raise NotImplementedError("Almost interface")

"""
Abstract class that implements IPrintable and provides a common behaviour for printing a message
"""
class GraphicShape(IPrintable):
    def calc_area(self):
        raise NotImplementedError("this method is abstract")

    def print_info(self):
        area = self.calc_area()
        print(f'{self.__class__.__name__} has an area of {area}')


"""
Implementation of a circle
"""
class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)


"""
Implementation of a square
"""
class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side


"""
Prints something that implements the interface
"""
def printSomething(printable: IPrintable):
    printable.print_info()


c = Circle(10)
printSomething(c)

s = Square(12)
printSomething(s)

try:
    shape = GraphicShape()
    printSomething(shape)
except:
    print("there was an error")
