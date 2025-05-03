li = [10,20,30,40]
print(type(li),li)  #<class 'list'> [10, 20, 30, 40]
iterator_object = iter(li)
print(type(iterator_object),iterator_object) #<class 'list_iterator'> <list_iterator object at 0x000001D81ECBAD40>

print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
# print(next(iterator_object)) #StopIteration

# 10
# 20
# 30
# 40


class CountUpTo:
    def __init__(self,limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUpTo(5)
for number in counter:
    print(number)

# 1
# 2
# 3
# 4
# 5


class EvenNum:
    def __init__(self,maxValue):
        self.maxValue = maxValue
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.maxValue:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration
        
maxValue = int(input())
even = EvenNum(maxValue)

for num in even:
    print(num)



# 10

# 0
# 2
# 4
# 6
# 8
# 10

class Fibonacci:
    def __init__(self,maxValue):
        self.maxValue = maxValue
        self.a,self.b = 0,1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < self.maxValue:
            fib_num = self.a
            self.a,self.b = self.b,self.a+self.b
            return fib_num
        else:
            raise StopIteration

maxValue = int(input())
fib = Fibonacci(maxValue)

for num in fib:
    print(num)

# 20

# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13

class Factorial:
    def __init__(self,maxValue):
        self.maxValue = maxValue
        self.current = 0
        self.fact = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.maxValue:
            raise StopIteration
        if self.current > 0:
            self.fact *= self.current
        result = self.fact
        self.current += 1
        return result
    
maxValue = int(input())
fact = Factorial(maxValue)

for num in fact:
    print(num)


# 5

# 1
# 1
# 2
# 6
# 24
# 120
