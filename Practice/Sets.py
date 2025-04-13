s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))
res = s1.symmetric_difference(s2)
res = sorted(res)
print("Symmetric difference of elements: ", res)

s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
s1 = set(s1)
s2 = set(s2)
common_ele = s1 & s2
print("Commeon elements: ",list(common_ele))

# 1 2 3 4 5
# 3 4 5 6 7
# Commeon elements:  [3, 4, 5]


s1 = set(list(map(int,input().split())))
s2 = set(list(map(int,input().split())))
d1 = s1-s2  #s1.difference(s2)
print(f"Elements in Set 1 but not in Set 2: ", d1)

# 1 2 3 4 5
# 3 4 5 6 7
# Elements in Set 1 but not in Set 2:  {1, 2}

s1 = set(list(map(int,input().split())))
s2 = set(list(map(int,input().split())))
if s1.isdisjoint(s2):  
    print("The sets are disjoint.")
else:
    print("The seta are not disjoint.")