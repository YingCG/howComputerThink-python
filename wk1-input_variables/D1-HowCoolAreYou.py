# let get some user information
banana = int(input("please type your age: "))
coolness = int(input("On the scale of 1-10, how cool are you? "))
result = banana * coolness

# here we stringify the result and throw it into print function
print("we expect you to live for " + str(result) + " years")

# # now we will try string templating, look back at the import statement at the top
# print("we expect you to live for $result years")

# it don't work as expected, let try different way of doing it

print(f"we expect you to live for {result} years!")
