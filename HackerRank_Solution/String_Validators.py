# # alnum: Checks for alphabets or numbers

# print('Kodnest123'.isalnum()) # True
# print('Kodnest*'.isalnum()) # False

# print('Kodnest'.isalpha()) #True
# print('code123'.isalpha()) # False

# print('12'.isdigit()) #True

# print('apple123'.islower()) #True
# print('BINDU#234'.isupper()) # True
# print('binDU'.islower())  #False

# print(any([10,20])) #True
# print(any((True,False,False,False))) #True
# print(any([False,False,False,False])) #False

 
#------------Logic-----------------------------

s = input()  #'qA2'

print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))

