# map(): is a method it will accept two parameter
#map(function, iterable_object) --> returns iterator object

def double(x):
    return x*2
li =[1,2,3,4]
double_li = list(map(double,li))
print(double_li) #[2, 4, 6, 8]



tup = ('10','20','30')
print(tup) #('10', '20', '30')
new_tup = tuple(map(int,tup))
print(new_tup) #(10, 20, 30)


li2 = [1,5,66]
print(li2) #[1, 5, 66]
new_li2 = list(map(float,li2))
print(new_li2) #[1.0, 5.0, 66.0]


