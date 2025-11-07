class goa:
    name=""
    drink=""
    def party(self):
        print("lets party!")
    def beach(self):
        print("enjoying the beach")

ramesh=goa()
suresh=goa()

ramesh.name="ramesh"
suresh.name="suresh"
ramesh.drink="yes"
suresh.drink="no"
print(ramesh.name)
print("drink :",ramesh.drink)
print(suresh.name)

print("drink :",suresh.drink)




class laptop():
    price=0
    procoessor=""
    ram=""


hp=laptop()
hp.price=20000
hp.processor="i5"
hp.ram="8gb"
print(hp.price)
