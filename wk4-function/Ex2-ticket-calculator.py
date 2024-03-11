# to calculate ticket price:
def gig_ticket_price_calculator(age, is_student=False):

    if is_student and age > 5:
        return 15.00

    if age <= 5:
        return 0.00
    elif age <= 18 or age > 65:
        return 20.00
    else:
        return 30.00


# Example usage
print("Gig Ticket price for age 65 is", gig_ticket_price_calculator(65))
print("Gig Ticket price for age 50 is", gig_ticket_price_calculator(50))
print("Gig Ticket price for age 50 (student) is", gig_ticket_price_calculator(50, True))
print("Gig Ticket price for age 5 is", gig_ticket_price_calculator(5))
print("Gig Ticket price for age 15 is", gig_ticket_price_calculator(15))
