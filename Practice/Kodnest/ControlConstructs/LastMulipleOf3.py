n = int(input())
original_num = n
multiple = -1
while(n>0):
    digit = n%10
    if(digit % 3 ==0):
        multiple = digit
    n = n//10
if(multiple != -1):
    print(f"The last multiple of 3 in {original_num} is {multiple}.")
else:
    print("No multiple of 3 found in ", original_num)
