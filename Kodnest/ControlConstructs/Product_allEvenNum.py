# n = int(input())
# product = 1
# i =1
# while(i<=n):
#     if(i%2==0):
#         product = product * i
#     i += 1
# print(f"The product of all even numbers up to {n} is {product}")


n = int(input())
product = 1
counter = 2
while(counter <=n):
    product = product * counter
    counter += 2
print(f"The product of all even numbers up to {n} is {product}")
