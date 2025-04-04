# li = list(map(int,input().split()))
# start = int(input())
# end = int(input())
# sub_li = li[start:end]
# print(f"Extracted sublist: {sub_li}")


# 1 2 3 4 5 6 7 8 9
# 2
# 5
# Extracted sublist: [3, 4, 5]


li = list(map(int, input().split()))
start = int(input())
end = int(input())

sub_li = []
for i in range(start,end):
    sub_li.append(li[i])
print(f"Extracted sublist: {sub_li}")
