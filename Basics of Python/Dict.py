'''
1. Dict is Mutable : You can change, add, or remove items after the dictionary is created..Keys Must Be Immutable, Values Can Be Any Data Type.
2. In dict we can store duplicate values  and In dict we cannot store duplicate key,
Stores Data as Key–Value Pairs.
3.Unordered (in Python < 3.7): From Python 3.7+, dictionaries preserve insertion order, but this is considered
an implementation detail before 3.7.

'''
# Syntax:
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

# Accessing Values
print(my_dict["name"])      # Output: Alice
print(my_dict.get("age"))   # Output: 25

# Adding or Updating Values
my_dict["age"] = 26         # Update
my_dict["country"] = "UK"   # Add new key-value

# Removing Items
my_dict.pop("city")     # Removes key "city"
del my_dict["age"]      # Deletes key "age"
my_dict.clear()         # Clears all items

# Iterating Over Dictionary
for key, value in my_dict.items():
    print(key, value)




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


