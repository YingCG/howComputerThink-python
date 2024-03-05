lineCounter = 1
size = input("Enter the Triangle Size: ")
while lineCounter <= int(size):
    starCounter = 0
    line = ""
    while starCounter < lineCounter:
        line = line + "*"
        starCounter = starCounter + 1
    print(line)
    lineCounter = lineCounter + 1
