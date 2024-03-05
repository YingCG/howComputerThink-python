counter = 0
result = ""
x = input("Enter your size of the triangle:")
while counter < int(x):
    if counter % 2 == 1:
        result = result + "-"
    else:
        result = result + "*"
    counter = counter + 1
print(result)
