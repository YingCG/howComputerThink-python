lineCounter = 1
while lineCounter <= 10:
    starCounter = 0
    line = ""
    while starCounter < lineCounter:
        line = line + "*"
        starCounter = starCounter + 1
    print(line)
    lineCounter = lineCounter + 1
