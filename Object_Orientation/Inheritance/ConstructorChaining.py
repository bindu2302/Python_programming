'''
Constructor chaining is  the process of calling 
one Constructor from another Constructor
'''

class GrandParent:
    def __init__(self):
        self.x = 100

class Parent(GrandParent):
    def __init__(self):
        self.y = 200
        super().__init__()

class Child(Parent):
    def __init__(self):
        self.z = 300
        super().__init__()

c = Child()
print(c.z) #300
print(c.y) #200
print(c.x) #100


