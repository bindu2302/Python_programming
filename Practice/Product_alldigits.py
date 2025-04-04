# 234 --> 24

num = int(input())
product = 1
num1 = num
while(num>0):
    digits = num %10
    product *= digits
    num = num //10
print(f"Product of digits {num1} is {product}")