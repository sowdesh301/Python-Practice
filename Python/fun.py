def painter(msg):
    print("message:",msg)

painter("paint my house")





def findevenorodd(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
    

b=int(input())
findevenorodd(b)



def findpassorfail(b):
    if(b>35):
        print("pass")
    else:
        print("fail")

a=int(input())
findpassorfail(a)


def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
    
a=int(input())
b=int(input())
printrange(a,b)
