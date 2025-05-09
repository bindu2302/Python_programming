#object. sort(): change original object
li = [10,5,3,20]
li.sort()
print(li) #[3, 5, 10, 20]
li.sort(reverse=True)
print(li) #[20, 10, 5, 3]

# sorted(ob): 
li2 = [100,30,500,10]
sorted(li2)
print(li2) #[100, 30, 500, 10]

sorted_li2 = sorted(li2)
print(sorted_li2) #[10, 30, 100, 500]