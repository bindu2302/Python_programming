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



# append() won't work with set
# pop ,del is not allowed for specific element


s1.add(500)
print(s1) #{True, 20, 'Kodnest', 500, 55.44, 10}

s1.remove(55.44)
print(s1)  #{True, 'Kodnest', 20, 500, 10}

popped_ele = s1.pop()  # pop() with without index  will delete and return one element 
print(popped_ele) #True


# del s1[2] # error

print(s1) # {20, 500, 'Kodnest', 10}

# Set Operations
s2 = {30,40,5,10}
print(s2)  # {40, 10, 5, 30}

s1_s2 = s1.union(s2)  # or s1|s2
print(s1_s2)  # {5, 40, 10, 20, 500, 'Kodnest', 30}

s1_s2 = s1.intersection(s2) # or s1&s2
print(s1_s2)  #{10}
