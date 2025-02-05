class Demo1:
    def __init__(self,name):
        self.__name = name   # Private Variable
   

d1 = Demo1('Akash')
# print(d1.__name)   #error
print(d1._Demo1__name)  # Akash  --> act as a public 


'''
1. Name Mangling  is the process of providing new 
name to the private variables.

2.These new names will be provided automatically
by python for all private members.

3. New Name will be privided in the format : 
objectName._className__variabelName

'''
class BankAccount:
    def __init__(self):
        self.__balance = 0  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. Current balance: {self.__balance}")
        else:
            print("Deposit failed. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. Current balance: {self.__balance}")
        elif amount > self.__balance:
            print("Withdrawal failed. Insufficient balance.")
        else:
            print("Withdrawal failed. Amount must be greater than 0.")

    def get_balance(self):
        return self.__balance

account = BankAccount()
deposit_amount = int(input())  
withdraw_amount = int(input())  
account.deposit(deposit_amount)
account.withdraw(withdraw_amount)