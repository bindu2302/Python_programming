li = list(map(int,input().split()))
d = {}
for i in li:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for num,count in d.items():
    print(f"{num} occurs {count} time(s)")