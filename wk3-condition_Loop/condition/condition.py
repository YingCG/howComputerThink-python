"""
Exercise 1: 
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
Ask user for their salary and year of service and print the net bonus amount.
"""

salary = float(input("Enter salary: "))
years_of_working = int(input("Enter years of service: "))

if years_of_working > 5:
    bonus = 0.05 * salary  # 5% bonus
    print(f"Congratulations! You have a bonus of {bonus:.2f}")
else:
    print(f"Your salary is {salary}")
