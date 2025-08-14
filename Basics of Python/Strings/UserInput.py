#input()will always takes an input as a string:
#Division Result will always be of type float.
num1 = int(input('Enter num1')) #20
num2 = int(input('Enter num2')) #10
print(f'Addition of {num1} and {num2} is {num1+num2}') #30
print(f'Subtraction of {num1} and {num2} is {num1-num2}') #10
print(f'Multiplication of {num1} and {num2} is {num1*num2}') #200
print(f'Division of {num1} and {num2} is {num1/num2}') #2.0

# 1. String Input (Default):
name = input("Enter your name: ")  # user types: Alice
print(name)       # Alice
print(type(name)) # <class 'str'>


# 2. Integer Input
age = int(input("Enter your age: "))  # user types: 25
print(age)        # 25
print(type(age))  # <class 'int'>

# 3. Float Input
price = float(input("Enter the price: "))  # user types: 99.99
print(price)        # 99.99
print(type(price))  # <class 'float'>

# 4. Boolean Input
is_active = input("Enter True or False: ")  # user types: True
is_active = is_active.lower() == "true"
print(is_active)      # True or False
print(type(is_active))# <class 'bool'>

# 5. Multiple Inputs in One Line
a, b = input("Enter two numbers: ").split()  # user types: 10 20
a = int(a)
b = int(b)
print(a + b)  # 30

# 6. List Input (Space-separated values)
nums = list(map(int, input("Enter numbers: ").split()))  # user types: 1 2 3 4
print(nums)        # [1, 2, 3, 4]
print(type(nums))  # <class 'list'>

# 7. Tuple Input
values = tuple(map(int, input("Enter numbers: ").split()))  # user types: 5 10 15
print(values)        # (5, 10, 15)
print(type(values))  # <class 'tuple'>

# 8. Complex Number Input
c = complex(input("Enter a complex number: "))  # user types: 2+3j
print(c)        # (2+3j)
print(type(c))  # <class 'complex'>
