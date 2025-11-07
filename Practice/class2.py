class phone():
    chargertype="B-Type"
    def  __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand :",self.brand)
        print("price ",self.price)
        print("chagertype :",self.chargertype)


readme=phone("readme","10000")
oppo=phone("oppo","20000")
readme.display()
oppo.display()


class laptop():
    
