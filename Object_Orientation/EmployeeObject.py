class Employee:
    company_name = 'code'  # Class based Variable

    def __init__ (self, name, age, designation):
        self.name = name     # instance varaibles
        self.age = age 
        self.designation = designation

    def login(self,time):  # instance method
        print(f'{self.name} logged in at {time}')
    
    def logout(self,time): # instance method
        print(f'{self.name} loggedout at {time}')
    
    def work(self,hours): # instance method
        print(f'{self.name} worked for {hours}')

    def getDetails(self):
        print('Employee Name:',self.name)
        print('Employee age:',self.age)
        print('Employee designation:',self.designation)


# Creating objects   
e1 = Employee('Bindu',23,'Junior Developer')
e2 = Employee('Kalyan',28,'DevOps Senior Engineer')
e3 = Employee('Vissu',26,'Digital Marketer')

e1.getDetails()
e1.login('9:30')
e1.logout('7:30')
e1.work('8:00')

e2.getDetails()
e2.login('10:00')
e2.logout('5:00')
e2.work('7:00')

e3.getDetails()
e3.login('9:00')
e3.logout('6:30')
e3.work('8:00')

