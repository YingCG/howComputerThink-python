# create a basic class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is  a secret"

    def getPrice(self):
        if hasattr(self, "discount"):
            return self.price - (self.price * self.discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self.discount = amount


# create instance of the class
book1 = Book("what is the color of the wind?", "Anne Herbauts", 36, 39.99)

# print the class and property
# print(book1.title)
# print(book1.getPrice())

book2 = Book("What Will The Weather Be Like Today", "Paul Rogers", 36, 49.99)
print(book2.getPrice())
book2.setDiscount(0.25)
print(book2.getPrice())
# print(book2.__secret)
print(type(book2))
