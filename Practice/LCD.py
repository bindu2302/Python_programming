def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm = greater
            break
        greater += 1

    return lcm
x = int(input())
y= int(input())
print(lcm(x,y))
# 2,3
# 6