class phone():
    chargertype="C-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("chargertype",self.chargertype)

phone.chargertype="b-type"
samsung=phone("sammsung",9000)
samsung.display()

oppo=phone("oppo",10000)
oppo.display()
