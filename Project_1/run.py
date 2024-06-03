"""
Ensure to complete the expected code in hpolyFintech.py before proceeding to this file
"""
from hpolyFintech import *

option = ['R', 'W', 'D', 'C', 'B', "EXIT"]


def align_center(message):
    print(message.center(100))


def align_tab(message):
    info = message.split("\n")
    for information in info:
        print(f"\t{information}")


def register_data():
    data_gen = {}
    align_center("Please Provide the following data correctly")
    data_gen["username"] = input("\tEnter username$ ")
    data_gen["pin"] = pin_validation()
    data_gen["amount"] = amounting()
    data_gen["age"] = age_validation()
    user_registration(**data_gen)


def deduct_data():
    cater = accountData()
    for item in cater:
        result = withdrawals(item['accountNumber'], item['pin'])
        align_tab(result)
        break

def checkings():
    cater = accountData()
    for item in cater:
        username = item["username"]
        pin = item["pin"]
        balance_result = check_balance(username,pin)
        align_tab(balance_result)
        break


def deposit_check():
    data = accountData()
    for item in data:
        username = item['username']
        account_number = item['accountNumber']
        credit = deposit(username,account_number)
        align_tab(credit)
        break

def bal_check():
    cater = accountData()
    for item in cater:
        username = item['username']
        pin = item['pin']
        backup = check_balance(username, pin)
        align_center(backup)
        break



def pin_validation():
    while True:
        try:
            pin = int(input("\tEnter user pin$ "))
            if len(str(pin)) == 4:
                return pin
            else:
                align_tab("Pin must be 4 digits")
        except ValueError:
            align_tab("Pin must be an integer data type")


def amounting():
    while True:
        try:
            amount = int(input("\tEnter initial deposit$ "))
            if amount >= 1000:
                return amount
            else:
                align_tab("Initial deposit must be up to 1000 and above")
        except ValueError:
            align_tab("Initial deposit must be an integer data type")

def withdrawals_validation():
    while True:
        try:
            amount = int(input("\tEnter amount to withdraw$ "))
            if amount >= 100:
                return amount
            else:
                align_tab("Amount must be up to 100")
        except ValueError:
            align_tab("Amount must be an integer data type")


def age_validation():
    while True:
        try:
            age = int(input("\tEnter age$ "))
            if age > 0:
                return age
            else:
                align_tab("Age must be a positive integer")
        except ValueError:
            align_tab("Age must be an integer data type")


while True:
    print("*" * 100)
    align_center("Welcome to HpolyFintech Service")
    print()
    align_center("Enter either [R to register, W to withdraw, D to deposit, C to check balance, B for balance]")
    align_center("Enter exit to close Application")

    choice = input("\t$ ")

    if choice.lower() == "r":
        register_data()
    elif choice.lower() == "w":
        deduct_data()
    elif choice.lower() == "d":
        deposit_check()
    elif choice.lower() == "b":
        bal_check()
    elif choice.lower() == "c":
        checkings()


        # Study the code above, depending on how you implemented the rest of your features like deposit, withdrawal, etc
        # in hpolyFintech.py, implement other choices to execute the needed functions
        # Ensure to use align_tab to print all text returned from your called functions if the text is aligned to
        # the left, or use align_center if the text is aligned to the center or use print function only
        # where it is crucial and necessary if any

    elif choice.lower() == "exit":
        print()
        align_center("GOOD BYE")
        print("*" * 100)
        break
