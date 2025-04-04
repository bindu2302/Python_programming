n = int(input("Enter the number of elements: "))
list1 = list(map(int, input("Enter the numbers: ").split()))
print("Unsorted list: ", list1)
for j in range(len(list1)):
    for i in range(len(list1)-1,j,-1):
        if list1[i] < list1[i-1]:
            list1[i], list1[i-1] = list1[i-1],list1[i]
print("Sorted list: ", list1)

# Enter the number of elements: 5
# Enter the numbers: 1 4 0 3 2
# Unsorted list:  [1, 4, 0, 3, 2]
# Sorted list:  [0, 1, 2, 3, 4]