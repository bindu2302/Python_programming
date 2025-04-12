li = list(map(int,input().split()))
max = li[0]
min = li[0]

for i in li:
    if i > max:
        max = i
    if i < min:
        min = i
print("The Maximum value is: ", max)
print("The Minimum value is: ", min)