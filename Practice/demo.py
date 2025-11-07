x,y=input("enter two numbers").split()
print("x is",x)
print("y is ",y)


age_input=input("enter a age")
age=int(age_input)
if (age<0):
    print("invalid age")
elif(age<18):
    print("minor")
elif(age>=18 and age<65):
    print("adult")
else:
    print("valid citizen")

color=input("enter the color")
print(color)

price=float(input())
print(price)

a="sowdesh"
b=10
c=9.0
d=["don","nice"]
e=("hi","cool")
f={"geek":1,"for":5}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
