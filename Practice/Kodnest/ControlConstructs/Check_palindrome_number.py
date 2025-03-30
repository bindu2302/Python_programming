# n = int(input())
# reverse_num = 0
# original_num = n
# while(n>0):
#     digit = n % 10
#     reverse_num = reverse_num * 10 + digit
#     n = n//10
# if(original_num == reverse_num):
#     print(f"The number is a palindrome")
# else:
#     print(f"The number is not a palindrome.")

# check string 
n = input()
original_string = n
reverse_str = ""
for i in n:
    reverse_str = i + reverse_str
if (original_string == reverse_str):
    print("palindrome")
else:
    print("not palindrome")