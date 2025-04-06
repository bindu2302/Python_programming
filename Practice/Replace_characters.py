def cipher_text(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            result += new_char
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result

# Take input from user
input_text = input("Enter text: ")
encrypted_text = cipher_text(input_text)
print("Encrypted Text:", encrypted_text)  #Encrypted Text:  Khoor Zruog!


