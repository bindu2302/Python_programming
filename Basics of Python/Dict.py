'''
1. Dict is Mutable
'''


d1 = {'name':"HimaBindu",'age': 27,'phone':23456,'age':29}
print(d1,type(d1)) #{'name': 'HimaBindu', 'age': 29, 'phone': 23456} <class 'dict'>

# In dict we cannot store duplicate key
d1['name'] = 'Pooja'
print(d1) #{'name': 'Pooja', 'age': 29, 'phone': 23456}

# In dict we can store duplicate values 
marks = {'Sci': 85,'Maths':85} # Allowed

for i in d1.keys():
    print(i)  # name age, phone

for i in d1.values():
    print(i) # Pooja, 29,23456


for i in d1.items():
    print(i) #('name', 'Pooja') ('age', 29) ('phone', 23456)


