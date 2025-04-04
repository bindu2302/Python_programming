# # 1
# # 12
# # 123
# # 1234
# # 12345

# n = int(input())
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(p,end="")
#         p += 1
#     print()

# # 12345
# # 1234
# # 123
# # 12
# # 1
# n = int(input())
# for i in range(i,-1,-1):
#     p = 1
#     for j in range(i+1):
#         print(j+1,end="")
#     print()


# # 1
# # 21
# # 321
# # 4321
# # 54321
# n = int(input())
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1,end="")
#     print()


# #  12345
# #   1234
# #    123
# #     12
# #      1
# n = int(input())
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         print(p,end="")
#         p += 1
#     print()



# #      1
# #     123
# #    12345
# #   1234567
# #  123456789
# n = int(input())
# for i in range(n):
#     p = 1
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i):
#         print(p,end="")
#         p += 1
#     for j in range(i+1):
#         print(p,end="")
#         p += 1
#     print()


# # 5 
# # 5 4
# # 5 4 3
# # 5 4 3 2
# # 5 4 3 2 1
# n = int(input())
# for i in range(n):
#     p = 5
#     for j in range(i+1):
#         print(p,end=" ")
#         p -= 1
#     print()


#  54321
#   4321
#    321
#     21
#      1


# n = int(input())
# k = 5
# for i in range(n):
#     p = k
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,n):
#         print(p,end="")
#         p -= 1
#     k -= 1
#     print()


#      1
#     121
#    12321
#   1234321
#  123454321
n = int(input())
for i in range(n):
    p = 1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
        p += 1
    for j in range(i+1):
        print(p,end="")
        p -= 1
    print()


# 1
# 23
# 456
# 78910
n = int(input())
p = 1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
        p += 1
    print()