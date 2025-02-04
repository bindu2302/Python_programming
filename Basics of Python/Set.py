'''
1. In Set we can store homogeneous as well as Heterogeneous Data.
2. Set is an Unordered Collection of Data.
3. Set does not support indexing of data.
4. In Set we cannot store duplicates.
5. Sets are Mutable.
'''

s1 = {10,True,'Kodnest',10,20,55.44}
print(s1,type(s1)) #{'Kodnest', True, 20, 55.44, 10} <class 'set'>
#print(s1[0]) #TypeError: 'set' object is not subscriptable


#add():
#append won't work with set

s1.add(500)
print(s1) #{True, 20, 'Kodnest', 500, 55.44, 10}

s1.remove(55.44)
print(s1)  #{True, 'Kodnest', 20, 500, 10}

# pop ,del is not allowed for specific element

poped_ele = s1.pop()  # pop() with without index  will delete and return one element 
print(poped_ele) #True


# del s1[2] # error

