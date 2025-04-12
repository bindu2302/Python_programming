tuple = tuple(list(map(int,input().split())))
n = int(input())

index = -1
for i in range(len(tuple)):
    if tuple[i] == n:
        index = i
        break
if index != -1:
    print(f"Element {n} found at index at {index}")
else:
    print(f"Element {n} not found in tuple")
