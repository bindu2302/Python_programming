class Student:
    college_name = 'Kodnest'
    def get_info(self):
        print("Colleg name is: " , Student.college_name)

    @classmethod
    def change_name(cls,new_name):
        cls.college_name = new_name

s1 = Student()
s1.get_info()  # Collge name is :Kodnest
Student.change_name('Code')
s1.get_info()  ## Collge name is :Code



class Employee:
    company_name = "Unknown"
    employee_count = 0

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.increment_employee_count()

    @staticmethod
    def company_policy():
        print("Company Policy: All employees must adhere to company ethics and integrity.")

    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1

company_name = input()
Employee.company_name = company_name 

name = input()
employee_id = input()
salary = float(input())

employee = Employee(name, employee_id, salary)

print(f"Updated Employee Count: {Employee.employee_count}")
print(f"Company: {Employee.company_name}")
print(f"Employee Count: {Employee.employee_count}")
print(f"Employee Name: {employee.name}, ID: {employee.employee_id}, Salary: {int(employee.salary)}")
Employee.company_policy()