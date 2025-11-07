class calculator():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
        print("sub",self.num1-self.num2)
        
obj1=calculator(12,3)
obj1.add()
obj1.sub()


class calculator():
    def add(self,a,b):
        print("Add",a+b)

obj1=calculator()
obj1.add(10,20)

