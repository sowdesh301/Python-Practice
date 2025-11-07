class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def display(self):
        print(self.name,self.grade)

s1=student("sowdesh","O")
s1.display()
        
        
class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")

c1=car()
c1.start()

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.dep=dep

    def display(self):
        print(self.name,self.salary,self.dep)
        
m1=manager("sowdesh","2000000","IT")
m1.display()
