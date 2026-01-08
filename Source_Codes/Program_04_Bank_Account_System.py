class Customer:
    account_no = 1000

    def __init__(self):
        self.name = input("Enter customer name: ")
        self.acno = Customer.account_no
        Customer.account_no += 1
        self.balance = 0
        print("Account created successfully for", self.name)
        print("Your Account Number is", self.acno)

    def deposit(self):
        amt = int(input("Enter deposit amount: "))
        self.balance += amt
        print("Deposit successful. Balance is", self.balance)

    def withdraw(self):
        amt = int(input("Enter withdraw amount: "))
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            print("Withdraw successful. Balance is", self.balance)

    def check_balance(self):
        print("Balance is", self.balance)

    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.acno)
        print("Balance:", self.balance)


customers = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        c = Customer()
        customers[c.acno] = c

    elif ch in [2, 3, 4, 5]:
        if not customers:
            print("No accounts exist. Please create an account first.")
            continue

        acno = int(input("Enter account number: "))
        if acno not in customers:
            print("Invalid account number")
            continue

        if ch == 2:
            customers[acno].deposit()
        elif ch == 3:
            customers[acno].withdraw()
        elif ch == 4:
            customers[acno].check_balance()
        elif ch == 5:
            customers[acno].display()

    elif ch == 6:
        print("Thanks for visiting. See you soon!")
        break

    else:
        print("Invalid choice")
