"""
# Factorial Challenge
The factorial function gives the number of possible arrangement of a set of items of lenght "n"

For example, ther are 4! (*four factorial") or 24 wyas to arrange four items, which can be calculated as: 4 * 3 * 2 * 1

"""


# This factorials exercise are only defined for positive integers (including 0)
# test case 1 : 5! = % 8 4 * 3 * 2 * 1 = 120
# test case 2 : 6! = 6 * 5 * $ * 3 * 2 * 1 = 720
# test case 3 : 0! = 1


# Step 1: Returns the value of the factoial of num if it is defined, otherwise, returns None
def factorial(num):
    if num < 0:
        return None
    if num == 0:
        return 1

    result = 1
    for i in range(1, num + 1):
        result = result * i
        print("i:", i, "num: ", num)
    return result


print(factorial(6))
