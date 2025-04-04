n = int(input())
last_even = -1
original_num = n
while(n>0):
    digit = n%10
    if(digit % 2 == 0):
        last_even = digit
        break
    n = n//10
if(last_even != -1):
    print(f"The last even digit in {original_num} is {last_even}")
else:
    print("No even digit found.")

