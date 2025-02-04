# n = 5
# k=5
# for i in range(n):
#     p=k
#     for j in range(i+1):
#         print(" ",end ="")
#     for j in range(i,n):
#         print(p,end="")
#         p -= 1
#     k -=1
#     print()



# def rev(n):
#     reve= ''
#     for i in n:
#         reve = i + reve
#     print(reve)

# n = input()
# rev(n)



def r(n):
    reverse_num =0
    while n>0:
        digit = n %10
        reverse_num = reverse_num*10+digit
        n = n//10
    return reverse_num

n = int(input())
result = r(n)
print(result)