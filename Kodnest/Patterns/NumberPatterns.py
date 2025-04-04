# 5
# 1
# 11
# 111
# 1111
# 11111

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("1",end="")
    print()


# 1
# 22
# 333
# 4444
# 55555
n = int(input())
p =1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p += 1
    print()


# 5
# 44
# 333
# 2222
# 11111

n = int(input())
p = 5
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p -= 1
    print()


# 0
# 22
# 444
# 6666
# 88888
n = int(input())
p = 0
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p += 2
    print()


# 0
# 22
# 444
# 6666
# 88888
n = int(input())
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print("1",end="")
        else:
            print("2",end="")
    print()



# 5
#      1
#     222
#    33333
#   4444444
#  555555555
#   6666666
#    77777
#     888
#      9
n = int(input())
p = 1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")
    p += 1
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    p += 1
    print()


# 5
#      1
#     222
#    33333
#   4444444
#  555555555
#   4444444
#    33333
#     222
#      1

n = int(input())
p = 1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")
    p += 1
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    p -= 1
    print()