class Bank:
    bank_name = 'SBI' 
    def __init__(self,name,age,bal):
        self.user_name = name
        self.age = age
        self.user_balance = bal
    
    def get_info(self):
        print(f'''User name is: {self.user_name}, User Balance : {self.user_balance} for
              Bank: {Bank.name}''')

b1 = Bank("pooja",26,55000)
print(b1.bank_name)  # SBI
print(Bank.bank_name)  # SBI
