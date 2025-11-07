class student():
    def __init__(self):
        self.name=""
        self.regno="1"
    def display(self):
        print("name",self.name)
        print("regno",self.regno)

s1=student()
s2=student()
s1.name="sowdesh"
s1.regno="95"

s2.name="magesh"
s2.regno="34"


s1.display()
s2.display()
