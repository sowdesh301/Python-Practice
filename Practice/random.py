import random
num=random.randint(1,20)

guess=int(input("can you guess the number i am  thinking? its less tham 20 :"))

while(num!=guess<5):
    attempts=attempts+1
    print("you lost")


while(num!=guess):
    if(guess>num):
        print("your guess is higher")
    else:
        print("your guess is lower")
    guess=int(input("Guess again!..."))
               
print("you won!")
