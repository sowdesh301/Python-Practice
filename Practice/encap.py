#private
class company():
    def __init__(self):
        self.__companyname="google"

    def companyname(self):
        print(self.__companyname)


c1=company()
c1.companyname()


#protected

class company():
    def __init__(self):
        self._companyname="google"

class b(company):
    pass

b1=b()
print(b1._companyname)
    
