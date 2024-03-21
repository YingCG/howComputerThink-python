class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getPrice(self):
        if hasattr(self, "discount"):
            # return self.price - self.discount
            return self.price - (self.price * self.discount)
        else:
            return self.price

    def setDiscount(self, percentage):
        self.discount = percentage / 100
        return self

    def __str__(self):
        price = str(self.getPrice())
        return f"Our book for sale:   {self.title} is now {price}"


# create an instance
book1 = Book("Harry Potter", "J. k. Rowling", 223, 22.50)
book2 = Book("Python", "Someone Smart", 500, 89.88)

# test 1
# print(book1)
print(book2)
book2.setDiscount(50)
print(book2)
