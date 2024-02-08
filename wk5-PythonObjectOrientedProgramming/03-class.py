counter = 0
result = ""

while counter < 10:
    if counter % 2 == 1:
        result += "-"
    else:
        result += "*"

    counter += 1

print(result)
