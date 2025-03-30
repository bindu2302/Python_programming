n = int(input())
k = n
sum = 0
while(n>0):
    digit = n % 10
    if(digit == 0):
        n = n//10
        continue
    sum = sum + digit
    n = n//10
print(f"The sum of non-zero digits in {k} is : {sum}")