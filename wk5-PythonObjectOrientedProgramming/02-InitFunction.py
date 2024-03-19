# Example 1
# create a basic class
class Book:
    def __init__(self, title):
        self.title = title


# create instance of the class
book1 = Book("Python")
book2 = Book("what is the color of the wind?")

# print the class and property
print(book2.title)


# Example 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 25)
print(person.name)  # Output: Alice
print(person.age)  # Output: 25
