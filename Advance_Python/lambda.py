from functools import reduce
li = [1,2,3,4,5]

# def even(ele):
#     return ele%2 ==0

# newli = list(filter(even,li))
# print(newli)


newli1 = list(filter(lambda num:num%2 == 0,li))
print(newli1) #[2, 4]


sum= reduce(lambda a,b:a+b,li)
print(sum) #15

square = list(map(lambda num:num**2,li))
print(square) #[1, 4, 9, 16, 25]