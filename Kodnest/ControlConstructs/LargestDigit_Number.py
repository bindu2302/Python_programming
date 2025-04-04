n = int(input())
largest_digit = 0
while(n>0):
    digit = n % 10
    if(digit > largest_digit):
        largest_digit = digit
    n = n//10
print(f"The largest digit is {largest_digit}")