n = int(input())
k = n
even_digits = ""
while(n>0):
    digit = n % 10
    if(digit % 2 != 0):
        n = n //10
        continue
    even_digits = str(digit) + " " + even_digits
    n = n//10
if(even_digits):
    print(f"The even digits in {k} are: " , even_digits.strip())
else:
    print(f"No even digits found in {k}")
