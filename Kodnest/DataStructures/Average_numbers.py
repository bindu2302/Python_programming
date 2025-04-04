# li = list(map(int,input().split()))
# avg = sum(li)/len(li)
# print(f"The average of the list is: {avg}")
          

li = list(map(int,input().split()))
total = 0
count = 0
for num in li:
    count += 1
    total += num
avg = total/count
print(f"The average of the list is: {avg}")
