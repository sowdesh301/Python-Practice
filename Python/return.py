def valueofa():
    return 10


a=valueofa()
print(a)



 
s_username="emc"
s_password=123

uname=input()
password=int(input())

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False

a=validate()
print(a)



a=int(input())
b=int(input())
c=int(input())

def add():
    return(a+b)*c

a=add()
print(a)



def add(n1,n2):
    return n1+n2

a=int(input())
b=int(input())
c=int(input())

added=add(a,b)
outpt=added*c
print(output)
