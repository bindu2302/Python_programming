# Rectangle pattern
rows = 5
col = 5
for i in range(rows):
    for j in range(col):
        print('*',end=" ")
    print()

print()

# right angled traingle  - increasing pattern
for i in range(rows):
    for j in range(i+1):
        print('*',end=" ")
    print()

print() 

# decreasing pattern
for i in range(rows):
    for j in range(i,rows):
        print("*",end=" ")
    print()


print()


# Right Pascal traingle 
rows = 4
col = 5
for i in range(rows):
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end=" ")
    print()


# butterfly Pattern
rows = 4
col = 5
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    print()



print()

# Diamond pattern

rows = 4
col = 5
for i in range(rows):
    for j in range(i,rows):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(1,rows):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,rows-1):
        print('*',end='')
    for j in range(i,rows):
        print('*',end='')
    print()



rows = 4  # Adjust this to control the size of the diamond

for i in range(rows):
    for j in range(rows - i):  # Leading spaces
        print(" ", end="")
    for j in range(2 * i + 1):  # Stars and spaces
        if j == 0 or j == 2 * i:  # Print '*' only at the boundaries
            print("*", end="")
        else:
            print(" ", end="")  # Inner spaces
    print()

# Lower half of the hollow diamond
for i in range(rows - 1, -1, -1):  # Avoid repeating the middle row
    for j in range(rows - i):  # Leading spaces
        print(" ", end="")
    for j in range(2 * i + 1):  # Stars and spaces
        if j == 0 or j == 2 * i:  # Print '*' only at the boundaries
            print("*", end="")
        else:
            print(" ", end="")  # Inner spaces
    print()






# remove leading spaces 

rows = 4  # Adjust this to control the size of the diamond

# Upper half of the hollow diamond
for i in range(rows):
    for j in range(rows - i - 1):  # Leading spaces (adjusted)
        print(" ", end="")
    for j in range(2 * i + 1):  # Stars and spaces
        if j == 0 or j == 2 * i:  # Print '*' only at the boundaries
            print("*", end="")
        else:
            print(" ", end="")  # Inner spaces
    print()

# Lower half of the hollow diamond
for i in range(rows - 1, -1, -1):  # Avoid repeating the middle row
    for j in range(rows - i - 1):  # Leading spaces (adjusted)
        print(" ", end="")
    for j in range(2 * i + 1):  # Stars and spaces
        if j == 0 or j == 2 * i:  # Print '*' only at the boundaries
            print("*", end="")
        else:
            print(" ", end="")  # Inner spaces
    print()


