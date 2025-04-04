n = int(input())
order = len(str(n))
sum = 0
temp = n
while(temp > 0):
    digit = temp % 10
    sum = sum + digit ** order
    temp = temp // 10
if(n== sum):
    print(n, " is a armstrong")
else:
    print(n, " is not armstrong")


# Number of n digits which are equal to the sum of n power of digits