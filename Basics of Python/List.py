'''
1. In List we can store homogenous as well as Heterogeneous data.
2. in List we can store Duplicate Values.
3. List is an Ordered Collection of Data: Order of insertion will remain as it is in the output
4. List are mutable: Once we declare a list we can modify it.
'''


li1 = [10,20,44,45,True,'Kodnest',20]
print(li1,type(li1))

#append(): will add element at the end of the list
li1.append(56)
print(li1) # [10, 20, 44, 45, True, 'Kodnest', 20, 56]

# insert(index,element): insert an ele at specified index
li1.insert(1,15)  
print(li1)  # [10, 15, 20, 44, 45, True, 'Kodnest', 20, 56]

#remove(ele):Removes the first occurance of the specified ele
li1.remove(20)
print(li1) #[10, 15, 44, 45, True, 'Kodnest', 20, 56]


# in and not in Operator:
print(2000 in li1) # false 
print('Kodnest' in li1)# True


#pop: without argument will delete and return last ele,from list

removed_ele = li1.pop()
print(removed_ele) 
print(li1) #56

#pop(index): With argument will delete the ele. at specified index
removed_ele = li1.pop(4)
print(removed_ele) #'Kodnest'
print(li1) #[10, 15, 44, 45, 'Kodnest', 20]


#del keyword:
# li1.pop(1)
del li1[1]
print(li1) #[10, 44, 45, 'Kodnest', 20]


del li1
#print(li1) # name li1 is not defined 