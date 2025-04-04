def unique_char(s):
    count_char = {}

    for char in s:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    
    for i in range(len(s)):
        if count_char[s[i]] == 1:
            return s[i],i
    return None
print(unique_char("aabb"))