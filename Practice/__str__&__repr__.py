class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person named {self.name}, age {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
p = Person("Alice", 30)
print(str(p))     #Person named Alice, age 30
print(repr(p))    #Person('Alice', 30)

print(p)      #Person named Alice, age 30