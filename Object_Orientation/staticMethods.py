class MathOperation:
    @staticmethod
    def add_numbers(a,b):
        return a+b
    def calci(self):
        pass
    
result = MathOperation.add_numbers(5,3)
print(result)   #8

math_op = MathOperation()
print(math_op.add_numbers(10,5))  #15
    
    