class grandpa():
    def phone(self):
        print("grandpa's phone")


class dad(grandpa):
    def money(self):
        print("Dad's money")


class son(dad):
    def laptop(self):
        print("son's laptop")


ram=son()
ram.laptop()
ram.money()

d1=dad()
d1.phone()



class dad():
    def money(self):
        print("dads money:")


class land():
    def important(self):
        print("important land")


class son1(dad,land):
    pass


class son2(dad):
    pass

class son3(dad):
    pass


ram=son1()
ram.money()
ram.important()

