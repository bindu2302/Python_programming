'''
Strong number: For a number, the sum of the factorial of each digit equals to the given number

'''
n = int(input())
s = 0
num = n
while(n>0):
    digit = n % 10
    fact = 1
    for i in range(1,digit+1):
        fact = fact * i
    s = s + fact
    n = n//10
if(s == num):
    print("Strong number")
else:
    print("Not a strong number")


# 145
# Strong number