class dad():
    def phone(self):
        print("dads phone")

class mom():
    def sweet(self):
        print("mom sweet")

class son(dad,mom):
    def laptop(self):
        print("sons laptop")

ram=son()
ram.laptop()
ram.phone()
ram.sweet()



class grandpa():
    def phone(self):
        print("grandpas phone")
        
class dad(grandpa):
    def money(self):
        print("dads money")



class son(dad):
    def laptop(self):
        print("sons laptop")

ram=son()
ram.laptop()

ram.money()
ram.phone()

hirarchical

class dad():
    def money(self):
        print("dads money")


class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s1=son2()
s1.money()


hybrid


class dad():
    def money(self):
        print("dads money")

class land():
    def important(self):
        print("important land")


class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s1=son2()
s1.money()






































