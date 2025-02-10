li = [10,20,30,40]
print(type(li),li)  #<class 'list'> [10, 20, 30, 40]
iterator_object = iter(li)
print(type(iterator_object),iterator_object) #<class 'list_iterator'> <list_iterator object at 0x000001D81ECBAD40>

print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
# print(next(iterator_object)) #StopIteration
