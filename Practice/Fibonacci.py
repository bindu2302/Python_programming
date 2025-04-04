def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
n = int(input())
print(fib(n))

# 6
# 8

def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
n = int(input())
for x in range(n):
    print(fib(x))

# 7
# 0
# 1
# 1
# 2
# 3
# 5
# 8

n = int(input())
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp + second

# 5
# 0
# 1
# 1
# 2
# 3