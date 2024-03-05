counter = 0
result = ""
while counter < 10:
    if counter % 2 == 1:
        result = result + "-"
    else:
        result = result + "*"
    counter = counter + 1
print(result)
