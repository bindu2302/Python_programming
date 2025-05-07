'''
1.Map: map() function applies to given function to each item in an iterable and rerturn map object
2. Filter: filter function selects items from an iterable based on condition, keeping only those the function return true.
3. reduce():from the functools module,reduces a list of items , reduces a list of items to single values by applying a function cummulatively.

'''

li = [1,2,3,4]

# map(function,iterable_object)
def double(num):
    return num * 2

double_li = list(map(double,li))
print(double_li)  #[2, 4, 6, 8]




# filter(function,iterable_object)
def checkEven(num):
    return num %2 ==0

even_li=list(filter(checkEven,li))
print(even_li) # [2,4]



#reduce()

from functools import reduce
def mul(a,b):
    return a * b

res = reduce(mul,li)
print("Multiplication is:", res) # Multiplication is: 24



def prime_generator(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

# Sample Input
n = int(input())

# Using the generator in a loop
for prime in prime_generator(n):
    print(prime)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temp = list(map(float,input().split()))
fahrenheit_temp = list(map(celsius_to_fahrenheit,celsius_temp))
print(fahrenheit_temp)

# 0 20 37 100
# [32.0, 68.0, 98.6, 212.0]

def to_upperCase(string):
    return string.upper()

user_input=input().split()
upper_strings = list(map(to_upperCase,user_input))
print(upper_strings)

# apple banana cherry
# ['APPLE', 'BANANA', 'CHERRY']


def isEven(num):
    return num % 2 == 0

user_input = list(map(int,input().split()))
even_num = list(filter(isEven,user_input))
print(even_num)

# 1 2 3 4 5 6
# [2, 4, 6]

from functools import reduce
def is_mul(x,y):
    return x * y

user_input = list(map(int,input().split()))
mul = reduce(is_mul,user_input)
print(mul)

# 2 3 5 10
# 300
