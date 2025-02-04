# string and tuple are immutable remainig mutable : -list,dict
def mutation(string,position,char):
    li = list(string)
    li[position] = char
    string = ''.join(li)
    return string


s = input()     #"bindu"
p,c = input().split() # ['2','k']
res = mutation(s,int(p),c) # [2,'k']
print(res)