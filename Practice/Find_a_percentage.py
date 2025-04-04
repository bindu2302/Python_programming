d = {}
n = int(input())
for i in range(n):
    name,*score = input().split()
    score = list(map(float,score))
    d[name] = score
    
target_name = input()
if target_name in d:
    avg = sum(d[target_name])/len(d[target_name])
    print(f"{avg:.2f}")
else:
    print("Error:name not found")