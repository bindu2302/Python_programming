# file = open('test.txt','r')
# print(file.read()) #  --> read the complete file
# print(file.readline()) # Hello from test file
# print(file.readlines())  #['Hello from test file\n', '\n', 'Learning file handling']
# print(data[0])  # H


# file1 = open('test2.txt','w')
# file1.write('Hello')
# file1.write('hello from python\n')
# file1.write('hello from Java')
# file1.close()


# file2 = open('test2.txt','a')
# file2.write('\nhello form java')
# file2.close()


with open('test.txt','r') as file:
    print(file.read())
