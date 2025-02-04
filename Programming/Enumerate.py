li = [10,20,30]
for idx,ele in enumerate(li):
    print(idx,ele) #0 10
                   #1 20
                   #2 30

li = list(map(int,input().split()))
for idx,ele in enumerate(li):
    print(f"Index of {ele} is {idx}")
#Index of 10 is 0
#Index of 20 is 1
#Index of 30 is 2

# write a python program to print even index element
li = [10,20,30,40]
for idx,ele in enumerate(li,start=1):
    if idx%2==0:
        print(ele) # 20 40


