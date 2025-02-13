num = int(input())

width = len(bin(num))-2
for i in range(1,num+1):

    dec = str(i).rjust(width)
    octal = oct(i)[2:].rjust(width)
    hexa = hex(i)[2:].upper().rjust(width)
    binary = bin(i)[2:].rjust(width)
    print(f"{dec} {octal} {hexa} {binary}")
