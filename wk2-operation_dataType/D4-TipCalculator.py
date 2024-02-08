# If the bill was $150.00, split between 5 people iwth 12% tip.
# Each person should pya (150.00/5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator ")

bill = float(input("What was the total bill? "))
print(f"The bill is {bill} ")

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tipAmount = (bill / 100) * tip
totalWithTip = bill + tipAmount
billPerPerson = totalWithTip / people
print(round(billPerPerson))
