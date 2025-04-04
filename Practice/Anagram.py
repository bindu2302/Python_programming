def is_anagram(str1,str2):
    str1,str2 = str1.lower(),str2.lower()

    if len(str1) != len(str2):
        return False
    
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
        
    for count in char_count.values():
        if count != 0:
            return False
    return True

str1 = input()
str2 = input()
print(is_anagram(str1,str2))



# silent
# listen
# True