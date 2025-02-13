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