n = 5
k = n
for i in range(1,n+1):
    print(i,k)
    k= k-1

# 1 5
# 2 4
# 3 3
# 4 2
# 5 



n = int(input())
if n > 1:
    for i in range(2,(n//2)+1):
        if n%i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("prime")

# 5
# 

str = input("Enter a String: ")
s = str.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))

# Enter a String: this is bindu
# bindu is this


n = 9
c = 1
k = n//3
for i in range(k+2,-1,-2):
    if(i%2!=0):
        print(c*" ",end="")
        print(i * "*")
        c = c+1

#  *****
#   ***
#    *


n = int(input())
sq = n * n

if str(sq).endswith(str(n)):
     print("Atomorphic")
else:
    print("Not Atomorphic")

# Enter a number: 76
# Automorphic