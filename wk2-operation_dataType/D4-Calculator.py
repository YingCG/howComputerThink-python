print("Welcome to our Calculator ")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
Sign = input("Select - or +")
if Sign == "+":
    Sum = x + y
else:
    Sum = x - y
print(f"The total is {Sum} ")
