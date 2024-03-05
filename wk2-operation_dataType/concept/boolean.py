# Booleans Casting
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool("lj"))
print(bool(0.0))
print(bool(0j))
print(bool("True"))
print(bool("False"))
print("bool(" ") :", bool(""))
print(bool([]))
print(bool([1, 2]))
print(bool({}))
print(bool(None))

# The reason we learn about casting in boolean as we don't use it this way,
# however it is important when we use in conditional statement or iteration
# Example below:
myList = [1, 2]
if myList:
    print("Mylist has some values in it!")

# Above is a simplify version of this:
if bool(myList):
    print("Yes we have this in the list!")

# another example
a = 5
b = 5
if a - b == 0:
    print("a and b are equal")
print(a == b)

# Boolean Logic
weatheIsNice = True
haveUmbrella = True
if not (haveUmbrella or weatheIsNice):
    print("Stay inside")
else:
    print("Go for a walk!")
