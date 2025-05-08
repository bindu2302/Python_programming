file = open('test.txt','r')
print(file.read()) #  --> read the complete file
print(file.readline()) # Hello from test file
print(file.readlines())  #['Hello from test file\n', '\n', 'Learning file handling']
# print(data[0])  # H


file1 = open('test2.txt','w')
file1.write('Hello')
file1.write('hello from python\n')
file1.write('hello from Java')
file1.close()


file2 = open('test2.txt','a')
file2.write('\nhello form java')
file2.close()


with open('test.txt','r') as file:
    print(file.read())


file = open("test3.txt",'r')
# content = file.read
# print(content)
# print(file.readline())  # Hello iam new file 

print(file.read())

file = open('test3.txt','w')
file.write("hi , how are you iam another new content")
file.close()

file = open('test3.txt','a')
file.write("\nThis is new line using append")
file.close()


with open('test3.txt','r') as file:
    content = file.read()
    print(content)
