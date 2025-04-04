def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n-1)
n = int(input())
result = fact(n)
print(result)

# 6
# 720

def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
    
n = int(input())
for i in range(n+1):
    print(fact(i))
    

# 1
# 1
# 2
# 6
# 24
# 120