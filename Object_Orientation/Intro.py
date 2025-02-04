class Student:
    def learn(self):
        print(self.name,'is learning')
    def play():
        print("Inside play method")
s1 = Student()
s1.name = 'Pooja'
print('Name is',s1.name)    #Name is Pooja   Pooja is learning
s1.learn()
# s.play() #TypeError: Student.play() takes 0 positional arguments but 1 was given

