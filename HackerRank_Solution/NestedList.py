n = int(input())
li =[]
for i in range(n):
    name = input()
    score = float(input())
    li.append([name,score])
print(li) #[['bindu', 100.0], ['kalyan', 99.0], ['vissu', 99.0]]

scores = []
for name,score in li:
    scores.append(score)

scores = list(set(scores))
scores.sort() #print(scores) [99.0, 100.0]


names_li =[]
second_smallest_score = scores[1]
for name,score in li:
    if score == second_smallest_score:
        names_li.append(name)
names_li.sort()
for name in names_li:
    print(name)
