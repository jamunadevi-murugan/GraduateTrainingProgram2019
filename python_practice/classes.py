# def A():
#     a=12
# def B():
#     b=a+1
#     print(b)
# A()
# B()

class B:
    # def __init__(self,name):
    #     self.name=name
    def disp(self,name):
        self.name = name

        print(self.name)
    def modify(self):
        self.name = 'Mr. ' + self.name
        print(self.name)

b=B()
b.disp('Oie')
b.modify()