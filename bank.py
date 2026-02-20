class BankAccount:
    # Class Attributes
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    # Constructor
    def __init__(self, account_holder, initial_deposit):
        self.account_holder = account_holder
        self.balance = initial_deposit

        # Update class data
        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print("Withdrawal successful!")

    # Display Account Info
    def display_account_info(self):
        print("\n----- Account Details -----")
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)
        print("----------------------------")


def main():
    accounts = {}

    while True:
        print("\n====== Bank Menu ======")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Display Bank Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            if name in accounts:
                print("Account already exists!")
            else:
                try:
                    deposit = float(input("Enter initial deposit: "))
                    if deposit < 0:
                        print("Initial deposit cannot be negative!")
                    else:
                        account = BankAccount(name, deposit)
                        accounts[name] = account
                        print("Account created successfully!")
                except ValueError:
                    print("Invalid input! Please enter numeric value.")

        elif choice == "2":
            name = input("Enter account holder name: ")
            if name in accounts:
                try:
                    amount = float(input("Enter deposit amount: "))
                    accounts[name].deposit(amount)
                except ValueError:
                    print("Invalid input! Please enter numeric value.")
            else:
                print("Account not found!")

        elif choice == "3":
            name = input("Enter account holder name: ")
            if name in accounts:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    accounts[name].withdraw(amount)
                except ValueError:
                    print("Invalid input! Please enter numeric value.")
            else:
                print("Account not found!")

        elif choice == "4":
            name = input("Enter account holder name: ")
            if name in accounts:
                accounts[name].display_account_info()
            else:
                print("Account not found!")

        elif choice == "5":
            print("\n----- Bank Summary -----")
            print("Bank Name:", BankAccount.bank_name)
            print("Total Accounts:", BankAccount.total_accounts)
            print("Total Bank Balance:", BankAccount.total_bank_balance)
            print("-------------------------")

        elif choice == "6":
            print("Thank you for using National Bank System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()