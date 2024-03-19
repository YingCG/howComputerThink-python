# create a basic class
class Book:
    def __init__(self, title):
        self.title = title


# create instance of the class
book1 = Book("Python")
book2 = Book("what is the color of the wind?")

# print the class and property
print(book2.title)
