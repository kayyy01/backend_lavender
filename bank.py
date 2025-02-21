# 🏦 Project Title: Advanced Bank ATM System
# 📌 Objective:
# Students will build a fully functional ATM system using Python that allows users to:
# ✅ Check their balance
# ✅ Deposit money (No negative deposits)
# ✅ Withdraw money (Check for sufficient balance)
# ✅ View transaction history
# ✅ Use a PIN for security
# ✅ Exit the system


# 📌 Requirements:
# 1. welcome message and action to continue
# 2. enter pin to continue to the ATM- 4 digit pin - numbers only
# 3. Display the menu
# 4. check balance againt an initial balance of 1000.00
# 5. deposit money - no negative deposits      
# 6. Withdraw money -check for sufficient balance
# 7. View transaction history (checking deposit and withdraw)
# 8. Exit the system


PIN = "1234"
balance = 1000.00


#checking balance
def check_balance():
    print(f"Your balance is {balance}")


#Withdraw Money
def withdraw( amount, balance):
    amount = float(input("Enter the amount you want to withdraw\n"))
    if  balance >amount > 0:
        balance = balance - amount
        print("Insufficient balance")
    elif amount <= 0:
        print("Invalid amount")
    else:
        balance = balance - amount

    print(f"Your new balance is {balance}")

# enter pin
def enter_pin():
    Pin = input("Enter your pin")
    match Pin:
        case "1234":
            print("Welcome!")
    



# pin = input("Welcome to the ATM. Your Money is Safe with Us\n Enter your 4 digit pin to continue\n")


# if pin != PIN:
#     print("Invalid Pin. Please try again")
#     pin = input("Enter your correct 4 digit pin to continue\n")




# else:
#     menu =     '''1. Check Balance
#     2. Deposit Money
#     3. Withdraw Money
#     4. View Transaction History
#     5. Exit the System'''


#     print(menu)
#     choice = int(input("Enter your choice\n"))


#     if choice == 1:
#         print(f"Your balance is {balance}")
