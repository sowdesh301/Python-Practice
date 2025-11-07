class laptop():
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp=laptop()
dell=laptop()
hp.ram="8GB"
hp.processor="i5"

dell.ram="16GB"
dell.processor="i7"

hp.display()
dell.display()

 
