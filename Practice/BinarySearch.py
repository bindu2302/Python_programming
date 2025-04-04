def Binary_search_first_occurrence(list1, key):
    low = 0
    high = len(list1) - 1
    index = -1

    while low <= high:
        mid = (low + high) // 2
        if key == list1[mid]:
            index = mid        # Save index
            high = mid - 1     # Continue searching on the left side
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if index != -1:
        print("Key is found at first occurrence index:", index)
    else:
        print("Key is not found")

# Input
list1 = list(map(int, input("Enter numbers: ").split()))
list1.sort()
print("Sorted List:", list1)
key = int(input("Enter key to search: "))

Binary_search_first_occurrence(list1, key)
