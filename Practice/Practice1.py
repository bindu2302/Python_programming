print(bool('Kodnest'))  # True
# print(int('Kod'))      # Error
print(int('11'))        # 11 ----> IMP Str(int) ---> Int
# print(float('Kodnest')) # Error
print(float('22.22'))   # 22.22 ---> IMP
print(bool(''))         # False
print(bool(0))          # False
print(bool(1))          # True
# print(int('12.56'))    # Error
print(int(12.56))       # 12

# Taking float value from the user and converting it into int
value = int(float(input('Enter price: Float value')))
print(value, type(value))



'''sample input = 10,20,30,40,20
 sample output = 20   Second Smallest element '''

li = list(map(int,input().split(',')))
li = list(set(li)) #[40, 10, 20, 30]
# li = li.sort()  # sort() won't return anything  -- None data will return
li.sort()
print(li) #[10, 20, 30, 40, 50]
print("Largest ele is: ",li[-1])
print("Second largest ele: ",li[-2])
print("Smallest ele: ",li[0])
print("second Smallest ele: ",li[1])



# Packing and Unpacking
name,*marks,age = ['Kodnest',10,20,30,18]
print(name) #Kodnest
print(marks) #[10, 20, 30]
print(age) #18


# store
''' 
sample input:
'Milk, 2.50'
'Egg, 2.50'
done

sample output:
Milk,  2.5
Egg, 2.5
'''
d = {}
while True:
    user_input = input().strip()
    if user_input.lower() == "done":
        break
    product,price = user_input.split(',')
    product = product.strip()
    price = float(price.strip())
    d[product] = price

for p,v in d.items():
        print(f"{p}: {v}")
