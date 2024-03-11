import random


def ticket_price_calculator(age, f_student=False):
    if f_student and age > 5:
        return 15.00
    elif age <= 5:
        return 0.00
    elif age <= 18 or age > 65:
        return 20.00
    else:
        return 30.00


def generate_random_seat():
    return random.randint(1, 100)


def buy_tickets():
    print("Welcome to the Ticket Booth!")

    total_price = 0.00

    while True:
        name = input("Enter your name (type 'exit' to stop): ")
        if name.lower() == "exit":
            break

        age = int(input("Enter your age: "))
        is_student = input("Are you a student? (yes/no): ").lower() == "yes"

        ticket_price = ticket_price_calculator(age, is_student)
        seat_number = generate_random_seat()

        print(f"\nTicket for {name}:")
        print(f"Ticket Price: ${ticket_price:.2f}")
        print(f"Seat Number: {seat_number}")

        total_price += ticket_price
        print(f"\nTotal Price so far: ${total_price:.2f}")

        more_tickets = input("Do you want to buy more tickets? (yes/no): ").lower()
        if more_tickets != "yes":
            break

    print(f"\nTotal Price for all tickets: ${total_price:.2f}")


buy_tickets()
