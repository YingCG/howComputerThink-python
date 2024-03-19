from datetime import date

class BankAccount():
    account_number: None
    account_holder: None
    balance: None
    opening_date: None

    # constructor
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0.00
        self.opening_date = date.today()

    # display all info
    def display_info(self):
        print("**** BANK ACCOUNT ****")
        print("account number:", self.account_number)
        print("account holder:", self.account_holder)
        print("balance:", self.balance)
        print("opening date:", self.opening_date, "\n")
    
    # deposit money onto bank account
    # parameter: sum - to deposit
    def deposit(self, sum):
        self.balance += sum

    # withdraw money from acoount
    # parameter: sum to withdraw
    def withdraw(self, sum):
        if sum > self.balance:
            print("incorrect ammount")
            return
        self.balance -= sum


