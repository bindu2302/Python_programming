# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(f"The factorail of {n} is {fact}")

start = int(input())
end = int(input())
fact = 1
for i in range(start,end+1):
    fact *= i
    print(f"The factorial of {i} : {fact}")
