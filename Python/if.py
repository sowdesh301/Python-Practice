salary=int(input())
age=int(input())
if(salary>=20000 or age<=25):
    loan=int(input())
    if(loan>50000):
        print("maximum is 50000")
    else:
        print("eligible for loan")
        print("eligible")
else:
    print("not eligible")
