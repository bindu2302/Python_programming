# input : I am Fine
# output: ['[I, 1]', '[am, 1]', '[fine, 2]']


def VowelCount(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split() 
    result = []

    for word in words:
        count = sum(1 for char in word if char in vowels)
        if count > 0:
            result.append(f"[{word}, {count}]")
    if not result:
        return ['There are no vowels contained in the string']
    return result

input = input()
print(VowelCount(input))


