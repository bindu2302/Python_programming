sentence = input()
li = sentence.split()
d = {}

for i in li:
    i = i.strip(".,!?;:")
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for word,count in d.items():
    print(f"{word}: {count}")


# This is a java program. Java is a oops.
# This: 1
# is: 2
# a: 2
# java: 1
# program: 1
# Java: 1
# oops: 1


# Simple contact book using dictinary
contact = {}
while True:
    user_input = input().strip()
    if user_input == 'done':
        break
    name,phoneno = user_input.split(",")
    phoneno = phoneno.strip()
    contact[name] = phoneno
for name,phoneno in contact.items():
    print(f"{name}: {phoneno}")

# Alice,555555
# Bob,4444444444     
# done

# Alice: 555555
# Bob: 4444444444


d = {}
while True:
    user_input = input().strip()
    if user_input.lower() == 'done':
        break
    product, price = user_input.split(",")
    product = product.strip()
    price = float(price.strip())
    d[product] = price

for product,price in d.items():
    print(f"{product}: {price}")

# milk,2.50
# bread,1.20
# eggs,3.00
# done

# milk: 2.5
# bread: 1.2
# eggs: 3.0