# li1 = [1,2,3,4,5]
# print(li1)  #[1, 2, 3, 4, 5]
# sq_li = []
# for i in li1:
#     sq_li.append(i**3)
# print(sq_li)  #[1, 8, 27, 64, 125]

li1 = [1,2,3,4,5]
dup_li = [i for i in li1]
 # when we have only if part then write it after for loop
even = [i for i in li1 if i%2==0]
sq_li = [i**i for i in li1]
new_li1 = [i+2 for i in li1]

# when we have if esle both writw it before for loop
even_odd = ['Even' if i%2==0 else 'Odd' for i in li1]


# Nested for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]

new_li = [ele for sublist in li1 for ele in sublist]
