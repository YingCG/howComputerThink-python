# def make_group(person1, person2):
#     group = [person1, person2]
#     return group

# or
make_group = lambda person1, person2: [person1, person2]

# Create two Person objects
person1 = "Alice"
person2 = "Bob"

# Make a group
group = make_group(person1, person2)
print("Group members:")
for person in group:
    print(person)
