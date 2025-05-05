'''
Decorator: A function in python that takes another function as input and add something extra to it, like layer of frosting.
it's like a wrapping a function inside a package to make it even better.Decorator helps you to add features like
logging, checking,timing without rewriting the original code.

@symbol: is used to easily apply a decorator to a function.
wrapper fucntion: The fucntion inside the decorator that add the extra functionality. 

 '''


def decor(func):
    def inner(name):
        if name == "Ayush":
            print(name, "Is learning Java")
        else:
            func(name)
    return inner

@decor
def choice(name):
    print(name,"is learning python")

choice("Ayush")   #Ayush Is learning Java
choice("Akash")  #Akash is learning python




def smartdiv(func):
    def inner(a,b):
        if b == 0:
            print("b should not be 0")
        else:
            func(a,b)
    return inner
    

@smartdiv
def div(a,b):
    print("Division is:", a/b)
div(10,2) #Division is: 5.0
div(10,0) #b should not be 0




def auth_decorator(func):
    def wrapper(username,password):
        if username=="admin" and password=="password":
            print("Authentication successful.")
            return func()
        else:
            print("Unauthorized")
    return wrapper

@auth_decorator
def secure_func():
    print("Hello, authenticated user!")
secure_func("admin","password")


# Authentication successful.
# Hello, authenticated user!


def logger_decorator(func):
    def wrapper():
        print("Starting function execution...")
        func()
        print("Function execution complete.")
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, world!")
say_hello()

# Starting function execution...
# Hello, world!
# Function execution complete.


def repeat_decorator(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()
        return wrapper
    return decorator

@repeat_decorator(times=3)
def say_hello():
    print("Hello, world!")
say_hello()

# Hello, world!
# Hello, world!
# Hello, world!
