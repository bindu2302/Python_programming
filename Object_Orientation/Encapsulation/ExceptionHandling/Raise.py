def checkAge(age):
    if(age<18):
        raise ValueError('Age must be greater than 18')
    
try:
    checkAge(12)
except ValueError as e:
    print('Error message: ', e)




class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")

account = BankAccount()

try:
    deposit_input = input()  
    deposit_amount = int(deposit_input.split(":")[-1].strip()) 
    account.deposit(deposit_amount)
except ValueError as e:
    print(f"Deposit failed. {e}")

try:
    withdraw_input = input()  
    withdraw_amount = int(withdraw_input.split(":")[-1].strip())  
    account.withdraw(withdraw_amount)
except ValueError as e:
    print(f"Withdrawal failed. {e}")


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")

account = BankAccount()
try:
    deposit_input = input()  # Read the entire input line
    deposit_amount = int(deposit_input.split(":")[-1].strip())  # Extract number after ":"
    account.deposit(deposit_amount)
except ValueError as e:
    print(f"Deposit failed. {e}")