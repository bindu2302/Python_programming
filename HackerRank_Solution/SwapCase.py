# sample input: HackerRank.com presents "Pythonist 2".
# sample output: hACKERrANK.COM PRESENTS "pYTHONIST 2".
s = input()
sample = ""
for i in s:
    if i.isupper():
        sample = sample + i.lower()
    else:
        sample = sample + i.upper()
print(sample)
