# 23476--> 7

num = int(input())
max = 0
num1 = num
while(num>0):
    digit = num % 10
    if(digit > max):
        max = digit
    num //= 10
print(f"The largest digit in {num1} is: {max}")