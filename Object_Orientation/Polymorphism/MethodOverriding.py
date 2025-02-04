# In this code we are achieving polymorphism using method overridding

class Calulator:
    def calculate(self,a,b):
        pass


class Add(Calulator):
    def calculate(self,a,b):
        print("Addition",a+b)


class Sub(Calulator):
    def calculate(self,a,b):
        print("Subtraction",a-b)


class Mul(Calulator):
   pass

ref = Add()
ref.calculate(10,20)

ref = Sub()
ref.calculate(20,10)

ref = Mul()
ref.calculate(10,20)

# Addition 30
# Subtraction 10