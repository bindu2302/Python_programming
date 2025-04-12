li = list(map(int,input().split()))  # 1 2 3 4 5
reverse_li = []
i = len(li) -1  # 4
while(i>=0):   # 4>=0, 3>=0,2>=0,1>=0
    reverse_li.append(li[i])  #5 ,4,3,2,1
    i -= 1  # 3,2,1,0
print("Reverse list: ", reverse_li)