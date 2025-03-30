n = int(input())
product = 1
while(n>0):
    digit = n % 10
    product = product * digit
    n = n//10
print(f"The product of all digits is ", product)