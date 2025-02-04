# li = input('Enter space separated Elements')
# print(li,type(li)) # 10 20 <class 'str'>

# li = li.split()
# print(li) # ['10','20']  # split() is used to convert string to list

# li = list(map(int,li))
# print(li) #[10, 20]




# tup = tuple(map(int,input('Enter space separated elements  ').split()))
# print(tup) #(45, 56, 4)


li = list(map(int,input().split())) #10 20 3 2 
print([i for i in li if i%2==0]) #[10, 20, 2]