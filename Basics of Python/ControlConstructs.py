# '''
# 1. Conditional : if,if-else,if-elif
# 2. Looping : for, while
# 3. Jumping : break, continue, pass

# '''

# # def checkAge(age):
# #     if(age>18):
# #         print("Age is greater than 18")
# #     else:
# #         print("Age is not greater than 18")
# # checkAge(18)


# # # WAP to display 'Child' if age is  below 18 , 
# # # display adult if age is above 18, display senior citizen if age is above 65.


# # def displayAgeCategory(age):
# #     if(age<18):
# #         print('Child')
# #     elif(age>18 and age<65):
# #         print('Adult')
# #     elif(age>65):
# #         print('Senior Citizen')
# #     else:
# #         print("not matching input")
# # displayAgeCategory(int(input('Enter age')))


# # For Loop

# '''
# for control_variable in iterable object
# '''
# for i in 'Kodnest':
#     print(i)


# for j in [10,20,30]:
#     print(j+5)

# for num in range(1,11):
#     print(num)

# #range(start,end-1,step)
# for i in range(11,21,2):
#     print(i,end=" ")

# print()

# for i in range(5):  # if one parameter it will become end
#     print(i,end=" ")

# # wAP to print all even num from 1 to 10
# print()
# for even_num in range(1,11):
#     if(even_num %2 ==0):
#         print(even_num)

# i=0
# while(i<10):
#     print(i+100)
#     i = i+1

#WAP to print numbers from 1-10 but if number is 6 then skip printing.
for i in range(1,11):
        if(i==6):
            continue
        print(i)
#WAP to print numbers from 1-10 but if number is 5 then stop printing.

for i in range(1,11):
        if(i==5):
            break
        print(i)


def disply():
      pass


