def show_balance(balance):
    print("\n" + "*" * 25)
    print(f"Your balance is: ${balance:.2f}")
    print("*" * 25 + "\n")

def deposit():
    while True:
        try:
            amount = float(input("Enter an amount to deposit: $"))
            if amount <= 0:
                print("Deposit amount must be greater than $0.00")
            else:
                print(f"${amount:.2f} has been successfully deposited.")
                return amount
        except ValueError:
            print("Please enter a valid number.")

def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter an amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be greater than $0.00")
            elif amount > balance:
                print("Insufficient funds. You cannot withdraw more than your balance.")
            else:
                print(f"${amount:.2f} has been successfully withdrawn.")
                return amount
        except ValueError:
            print("Please enter a valid number.")

def main():
    balance = 0.0
    options = {
        '1': "Show Balance",
        '2': "Deposit",
        '3': "Withdraw",
        '4': "Exit"
    }

    while True:
        print("\n" + "*" * 25)
        print("   Welcome to the Banking Program")
        print("*" * 25)
        for key, value in options.items():
            print(f"{key}. {value}")
        print("*" * 25)

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("\nThank you for using the Banking Program. Have a nice day!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
