# def linear(list1,key):
#     for i in range(len(list1)):
#         if(key==list1[i]):
#             print("key found at index ", i)
#             break
#     else:
#         print("not found")

# list1 = [23,3,52,2]
# key = 2
# linear(list1,key)


def linearSearch(list1,key):
    for i in range(len(list1)):
        if(key==list1[i]):
            print("key found at index: ",i)
            break
    else:
        print("not found")

list1 = list(map(int,input().split()))
key = int(input())
linearSearch(list1,key)


# 45 6 7 8 9 0 1
# 2 
# not found