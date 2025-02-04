class Calculator:
    def calculate(self,a,b):
        print('Calculate result of a and b')

class Add(Calculator):
    def calculate(self, a, b):
       print('Addition is:', a+b)

class Sub(Calculator):
    def calculate(self, a, b):
        print("Subtraction:", a-b)

ref = Add()
ref.calculate(10,20)  # 30

ref = Sub()
ref.calculate(20,10)  #10