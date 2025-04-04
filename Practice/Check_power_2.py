# def check_power_2(n):
#     return n>0 and (n&(n-1)) == 0
# print(check_power_2(19))


full_name = "John Michael Doe"

name_parts = full_name.split()
initials_part = f"{name_parts[0]} {name_parts[1][0]}. {name_parts[2][0]}."
print(name_parts)
print(initials_part)
