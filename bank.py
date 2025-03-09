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
transaction_history = []

def check_balance():
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter the amount you want to deposit: $"))
    if amount > 0:
        balance += amount
        transaction_history.append(f"Deposited: ${amount:.2f}")
        print(f"Successfully deposited ${amount:.2f}.")
    else:
        print("Deposit amount must be positive.")

def withdraw():
    global balance
    amount = float(input("Enter the amount you want to withdraw: $"))
    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        balance -= amount
        transaction_history.append(f"Withdrew: ${amount:.2f}")
        print(f"Successfully withdrew ${amount:.2f}.")
    
def view_transaction_history():
    if transaction_history:
        print("Transaction History:")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions made yet.")

def enter_pin():
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == PIN:
            print("Welcome!")
            return True
        else:
            attempts -= 1
            print(f"Invalid PIN. You have {attempts} attempts left.")
    print("Too many failed attempts. Exiting.")
    return False

def main():
    print("Welcome to the ATM. Your Money is Safe with Us.")
    
    if not enter_pin():
        return

    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            view_transaction_history()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()