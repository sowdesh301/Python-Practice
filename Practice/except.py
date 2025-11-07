try:
    a=int(input())
    b=int(input())
    print(a+b)

except Exception as e:
    print("something",e)

finally:
    print("something")

try:
    a=int(input())
    b=int(input())
    c=input()
    print(d)
except ValueError as e:
    print("value error")
except TypeError as e:
    print("Typr error")
except Exception:
    print("somthing wrong")
