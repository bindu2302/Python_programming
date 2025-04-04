def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
a = int(input())
b = int(input())
print(gcd(a,b))

# 4,18
# 2

num1 = int(input())
num2 = int(input())

if gcd(num1,num2) == 1:
    print("co-primes")
else:
    print("not co primes")