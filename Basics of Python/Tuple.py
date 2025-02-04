'''
1. In Tuple we can store homogeneous as well as Hetergenous data.
2. In tuple we can store duplicates
3. Tuples are ordered collection of data
4. Tuples are Immutable: Once we declare the tuple we cannot modify it.
'''

tup1 = (10,22.55,'Kodnest',True,10)
print(tup1) #(10, 22.55, 'Kodnest', True, 10)
# tup1.append(400)
# tup1.remove(55)
# tup1.pop()
# del tup1[2]
print(tup1[2]) #'Kodnest'
del tup1 # Remove entire tuple, deletes the complete object
# print(tup1) # error


t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3) # (1,2,3,4,5,6)




# Create singleton Tuple:

tup = (10,)
print(tup,type(tup)) #(10,) <class 'tuple'>


new_tup = (10,20,30,40)
# ele1 = new_tup[0]
# ele2 = new_tup[1]


# Unpacking of tuple
ele1,ele2,ele3,ele4 = new_tup
print('Value of ele1',ele1)
