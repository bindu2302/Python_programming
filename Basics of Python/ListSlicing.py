#list_name[start:end-1:steps]

li1 = [10,20,30,40,50,60]
sub_list = li1[0:4:1] 
print(sub_list) #[10, 20, 30, 40]

sub_list2 = li1[1::]
print(sub_list2) #[20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3) #[10, 30, 50]

rev_li = li1[::-1]
print(rev_li) #[60, 50, 40, 30, 20, 10]


print(li1[-1::]) #60




'''
Q: What is List Slicing?
Is used to create sublist from main list.
Syntax: list_name [start:end-1:steps]

reverse list: [::-1]
last ele: [-1::]

'''


