''' 
Generators: Geneartors are special functions in python produces items only when you need them (returns value when we need them)
saving memory and make your programs more efficiently, it handle large datasets like millions of customer records needed, it fetches item one 
at a time.

Yield: A keyword use to pause the generator and remember where it left off, to continue next time when call the function.

Generator expression: it is like list comprehension to create generator using on line only.

'''

# def disp():
#     return 10
#     return 20
#     return 30

# print(disp()) #10
# print(disp()) #10
# print(disp()) #10



def generator_function():
    print("Hello")
    yield 10
    yield 20
    yield 30

generator = generator_function()

print(generator_function) #<function generator_function at 0x000001F92AF91440>
print(next(generator)) #10
print(next(generator)) #20
print(next(generator)) #30
# print(next(generator)) #StopIteration

# Hello
# 10
# 20
# 30





def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        print(a)
        a,b = b, a+b


fibonacci(10)


def fibonacci_gen(num):
    a,b = 0,1
    for i in range(num):
        yield a
        a,b = b, a+b


ref = fibonacci_gen(10)
print(next(ref)) # 0
print(next(ref)) # 1
print(next(ref)) # 1
print(next(ref)) # 2

for i in range(5):
    print(next(ref))



def factorial_generator(max_value):
    current = 0
    factorial = 1

    while current <= max_value:
        if current == 0:
            yield 1
        else:
            factorial *= current
            yield factorial
        current += 1

max_value = int(input())
fact = factorial_generator(max_value)
for num in fact:
    print(num)


# 5

# 1
# 1
# 2
# 6
# 24
# 120


def prime_generator(max_value):
    def isPrime(n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    for num in range(2,max_value+1):
        if isPrime(num):
            yield num

max_value = int(input())

for n in prime_generator(max_value):
    print(n)


# 20

# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19

def square_gen(max_value):
    current = 1

    while current ** 2 <= max_value:
        yield current ** 2
        current += 1

max_value = int(input())
for n in square_gen(max_value):
    print(n)


# 20

# 1
# 4
# 9
# 16
