# BMI Calculator

# 1st inut: enter height in centremeters e.g: 165cm
height = input("Your Height: ")

# 2nd input: enter weight in kilograms e.g. 72kg
weight = input("Your Weight: ")

BMI = (float(weight) / float(height) ** 2) * 10000
print(BMI)
