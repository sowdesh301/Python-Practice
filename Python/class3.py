class fruit():
    def __init__(self,col):
        self.color=col
    
apple=fruit("red")
print(apple.color)

        
class teacher():
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name",self.name)
        print("regno",self.regno)

t1=teacher("pushpa",121)
t2=teacher("radha",234)
t1.display()
t2.display()
