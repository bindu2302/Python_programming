# object.reverse() will reverse the original object
li = [10,5,20,7,40]
print('Before reverse: ', li)
li.reverse()
print('After reverse: ',li) #After reverse:  [40, 7, 20, 5, 10]


#list/tuple/set(reversed(iterable_object)):
li2 = [11,6,8,22]
reverse_li2=list(reversed(li2))
print(li2) #[11, 6, 8, 22]
print(reverse_li2) #[22, 8, 6, 11]


#practice:
li3 = [1,5,2,9]
li3.reverse() # reversing original list
new_reverse_li3 = list(reversed(li3))  # --> creating new reverse list
print(li3) # [9, 2, 5, 1]
print(new_reverse_li3) #[1, 5, 2, 9]
