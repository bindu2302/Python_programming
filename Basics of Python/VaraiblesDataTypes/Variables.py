1. Basic Variable Examples

# Integer variable
age = 25

# Float variable
price = 99.99

# String variable
name = "Alice"

# Boolean variable
is_active = True


2. Multiple Assignments
# Assign the same value to multiple variables
x = y = z = 10

# Assign different values in a single line
a, b, c = 5, "Hello", 3.14

3. Changing Variable Values
count = 10
print(count)   # Output: 10

count = 20     # Value changed
print(count)   # Output: 20

4. Variables with Different Data Types
student_name = "John"       # str
student_age = 21            # int
student_gpa = 3.8           # float
is_graduated = False        # bool

5. Using Variables in Expressions
x = 5
y = 10
total = x + y
print(total)   # Output: 15


6. Naming Rules for Variables
✅ Can contain letters, numbers, and underscores (_)
✅ Must start with a letter or underscore
✅ Case-sensitive (name and Name are different)
❌ Cannot use Python keywords (if, for, class, etc.)

Example of valid and invalid:
# Valid
user_name = "Bob"
_userID = 101
score2 = 99

# Invalid
2score = 99   # ❌ starts with number
for = 5       # ❌ keyword
