n = int(input())
s = 0
while n > 0:
    digit = n % 10
    s = s*10+digit
    n = n//10
print(s)

# 12345
# 54321