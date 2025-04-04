# 10 --> 3840

num = int(input())
product = 1
i =1
while(i<=num):
    if(i%2 == 0):
        product = product * i
    i += 1
print(f"The product of {num} is: {product}")
