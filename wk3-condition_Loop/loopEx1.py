"""
Excercise 0 --> print below: *-*-*-*-*-
"""
# num = 6
# while num > 0:
#     print("*")
#     num = num - 1
#     if num % 2 == 0:
#         print("-")

num = 10
line = ""
while num > 0:
    if num % 2 == 0:
        line += "*"
    else:
        line += "-"
    num = num - 1
print(line)

# --------------------------------------------------------------------------------------- #

"""
Excercise 1 --> print below:

*
**
***
****
*****
******

"""
num = 0
while num <= 5:
    line = "*"
    num = num + 1
    print(line * num)

    # --------------------------------------------------------------------------------------- #
    """
Excercise 2 --> print below:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
    
    """

counter = 1
while counter < 6:
    line = str(counter) + " "
    print(line * counter)
    counter += 1
