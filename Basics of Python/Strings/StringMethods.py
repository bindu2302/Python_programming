# Different ways of declaring the strings
s1 = "I'm Bindu"
s2 = 'My "age" is 23'
s3 = """We are learning
 Strings"""
s4 = '''Python is dynamically
 typed language'''
print(s1)
print(s2)
print(s3)
print(s4)

# More Operations on strings
# 1. Accessing characters in a string

word ="Python"
print(word[0]) # P
print(word[-1]) # n

# 2. Slicing Strings
Name = "Hima Bindu!"
print(Name[0:4]) # Hima
print(Name[5:]) #Bindu!
print(Name[:-1]) # Hima Bindu!
print(Name[::-1]) # !udniB amiH


#3. Finding the Length of a String
message = "Welcome to Python!"
print(len(message)) # 19

#4.Changing the Case
greeting = "Hello, world"
print(greeting.upper()) # HELLO, WORLD
print(greeting.lower()) # hello, world

#5.Finding the Substring in a String
text = "Learning Python is fun!"
print(text.find("Python")) # 9  -->returns -1 if not found
print("fun" in text)  # true

#6.Replacing parts of a String
sentence = "I Like java."
new_sentence = sentence.replace("java","python")
print(new_sentence)  #I Like  python.


#7. Splitting and Join
text= "My name is Bindu"
text_list=text.split()
text_string = '-'.join(text_list)
print(text_list) #['My', 'name', 'is', 'Bindu']
print(text_string) # My-name-is-Bindu



