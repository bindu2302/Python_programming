'''
Method chaining is  the process of calling 
one method from another method
'''

class GrandParent:
    def cook(self):
        print("Granparent can cook Biryani")

class Parent(GrandParent):
    def cook(self):
        print("Parent can cook Maggie")

class Child(Parent):
    def cook(self):
        print("Child wont cook")
        super().cook()
        super(Parent,self).cook()  # Grandparent method will invoke

c = Child()
c.cook()

#Child wont cook
#Parent can cook Maggie
#Granparent can cook Biryani