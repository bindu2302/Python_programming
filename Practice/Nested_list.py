# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

n = int(input())
li = []
scores_li = []
for i in range(n):
    name = input()
    score = float(input())
    scores_li.append(score)
    li.append([name,score])

scores_li = list(set(scores_li))
scores_li.sort()
second_lowest_score = scores_li[1]

names = []
for name,score in li:
    if score == second_lowest_score:
        names.append(name)

names.sort()
for i in names:
    print(i)

