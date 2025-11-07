score=int(input())
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
elif(score>70):
    print("good student")
else:
    print("invalid score")
