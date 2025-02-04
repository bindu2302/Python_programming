class Demo:
    def disp(self):
        print('Inside disp with 0 para')
    def disp(self,a):
        print('Inside disp with 1 para')
    def disp(self,a,b):
        print('Inside disp with 2 para')

d = Demo()
# d.disp()
# d.disp(10)
d.disp(10,20)   #Inside disp with 2 para