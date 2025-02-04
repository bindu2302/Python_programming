'''Dunder Methods: The methods which has suffix and prefix as underscore(__)
these dunder methods can be called as Magic methods 
'''

class Demo1:
    def __str__(self):
        return "Hello"
    def __add__(self,other):
        self.a = 20
        other.b = 30
        return self.a + other.b


class Demo2:
    def __str__(self):
        return "HI"
        
d1 = Demo1()
d2 = Demo2()
'''In python if we print reference varraible then
it will display string represntation of an address of an object 

In the above exmaples we have overridden
 __str__ methods in their respective classes'''

print(d1)  #<__main__.Demo1 object at 0x000001D55C936A50>
print(d2) #<__main__.Demo2 object at 0x000001F5E5AE6CF0>
# print(d1+d2)

class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        print("Calculationg area:...")

class Circle(Shape):
    def __init__(self,name):
        super().__init__(name)
    def area(self):
        print(f"{self.name}: Area of circle : pi * r^2")
    
class Square(Shape):
    def __init__(self,name):
        super().__init__(name)
    def area(self):
        print(f"{self.name}:  Area of square: side * side")

circle_name = input()
square_name = input()
circle = Circle(circle_name)
square = Square(square_name)
circle.area()
square.area()

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says: Meow! Meow!")

dog_name = input()
cat_name = input()

dog = Dog(dog_name)
cat = Cat(cat_name)

dog.make_sound()
cat.make_sound()
