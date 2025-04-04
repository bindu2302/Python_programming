n = int(input())
if n > 0:
    for i in range(2,(n//2)+1):
        if n % i ==0:
           print("not a prime")
           break
    else:
        print("is a prime")
else:
    print("is not a prime")

# 8
# not a prime
        

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, (n//2) + 1):
        if(n%i==0):
           return False
    else:
        return True
n = int(input())

if(isprime(n)):
    print(n , "is a prime")
else:
    print(n , " is not a prime")

# 8
# 8 is not a prime