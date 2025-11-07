def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(10,20,30)


class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dogs barks")


class bird(animal):
    def sound(self):
        print("bird sing")
    


d1=bird()
d1.sound()
