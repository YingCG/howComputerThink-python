def make_group(person1, person2):
    group = [person1, person2]
    return group


# make_group = lambda person1, person2: [person1, person2]

# create object
student1 = "Jame Bond"
student2 = "Batman"

# calling the funtion
print(f"Group 1: {make_group(student1, student2)}")
group2 = make_group("somebody", "anotherbody")
print(f"Group 2: {group2}")

shopping_cart = ["kiwi", "feijoa"]
shopping_cart.append("chili")
print(shopping_cart)
shopping_cart.remove("feijoa")
print(shopping_cart)
