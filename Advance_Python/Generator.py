# def disp():
#     return 10
#     return 20
#     return 30

# print(disp()) #10
# print(disp()) #10
# print(disp()) #10



def generator_function():
    print("Hello")
    yield 10
    yield 20
    yield 30

generator = generator_function()

print(generator_function) #<function generator_function at 0x000001F92AF91440>
print(next(generator)) #10
print(next(generator)) #20
print(next(generator)) #30
# print(next(generator)) #StopIteration

# Hello
# 10
# 20
# 30