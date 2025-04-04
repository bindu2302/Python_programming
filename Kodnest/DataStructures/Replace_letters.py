def cipher_text(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char)- ord('a') + 3)% 26 + ord('a'))
            result += new_char
        elif 'A'<=char<='Z':
            new_char = chr((ord(chr) - ord('A') + 3) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result


import unittest  

class TestCipherText(unittest.TestCase):  
    def test_lowercase(self):  
        self.assertEqual(cipher_text("abc"), "def")  
        self.assertEqual(cipher_text("xyz"), "abc")  
    def test_uppercase(self):  
        self.assertEqual(cipher_text("ABC"), "DEF")  
        self.assertEqual(cipher_text("XYZ"), "ABC")  
    def test_mixed_case(self):  
        self.assertEqual(cipher_text("aBcD"), "dEfG")  
    def test_non_alphabetic(self):  
        self.assertEqual(cipher_text("a1b2c3"), "d1e2f3")  
        self.assertEqual(cipher_text("hello, world!"), "khoor, zruog!")  
if __name__ == "__main__":  
    unittest.main()  