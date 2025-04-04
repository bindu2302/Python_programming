n = int(input())
result = 0
for i in range(1,n):
    if(n%i==0):
        result = result + i
if(result == n):
    print(n , " is  a perfect num")
else:
    print(n , " is not a perfect num")
# 6
# 6  is  a perfect num

l = int(input())
u = int(input())
for n in range(l,u):
    result = 0
    for i in range(1,n):
        if(n%i==0):
            result = result + i
    if n == result:
        print(n)