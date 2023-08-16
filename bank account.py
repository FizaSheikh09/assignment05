class BankAccount:
    def set_account_details(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Information\nAccount Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance:.2f}")


# Create an object of the BankAccount class
account = BankAccount()

# Set account details
account.set_account_details(account_number="123456789", account_holder_name="John Doe", initial_balance=1000.0)

# Deposit and withdraw money
account.deposit(500.0)
account.withdraw(200.0)

# Display account information
account.display_account_info()