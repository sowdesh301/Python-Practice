def add():
    a=int(input())
    b=int(input())
    print(a+b)

add()


def oddoreven(a):
    if(a%2==0):
        print("pass")
    else:
        print("fail")

a=10
oddoreven(a)

def printrange(a,b):
    for i in range(a,b):
        print(i)

a=int(input())
b=int(input())
printrange(a,b)





def add(n1,n2):
   return n1+n2

a=int(input())
b=int(input())
c=int(input())

added=add(a,b)
output=added*c
print(output)


def paint():
    return "ok"

msg=paint()
print(msg)
