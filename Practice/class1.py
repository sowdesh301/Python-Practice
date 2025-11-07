class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram :",self.ram)
        print("processor :",self.processor)
        


hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.processor="i5"

dell.ram="16gb"
dell.processor="i7"

hp.display()
dell.display()


class teacher():
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name:",self.name)
        print("regno :",self.regno)

t1=teacher("sowdesh","1")
t2=teacher("magesh","2")
t1.display()
t2.display()
