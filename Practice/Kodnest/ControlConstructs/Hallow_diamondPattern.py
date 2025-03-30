rows = int(input())

for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(rows-1,-1,-1):
    for j in range(rows-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()