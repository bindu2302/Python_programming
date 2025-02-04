'''
1. work() -- specialized method  -- only in child class
2.cook() -- overridden method -- used as it is in child class
3. play() --- inherited method -- change the implementation in child class

'''

class Student:
    def cook(self):
        print("Student is cooking")
    def play(Self):
        print("playing cricket")

class Employee(Student):
    def work(self):
        print("Employee is working")
    def cook(self):
        print("Employee is cooking")

e = Employee()
e.play()
e.cook()
e.work()

# playing cricket
# Employee is cooking
# Employee is working