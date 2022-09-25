import random
print("WELCOME TO THE GAME")
t=3
cpoint=0
hpoint=0
F=1
def neutral(x):
    if (x==1):
        return("s")
    elif(x==2):
        return("p")
    else:
        return("k")
def game(x,y):
    if(x=="s" and y=="p"):
        print("computer won this round")
        return(0)
    elif(x=="s" and y=="k"):
        print("you won this round")
        return(1)
    elif(x=="p" and y=="s"):
        print("you won this round")
        return(1)
    elif(x=="p" and y=="k"):
        print("computer won this round")
        return(0)
    elif(x=="k" and y=="s"):
        print("computer won this round")
        return(0)
    elif(x=="k" and y=="p"):
        print("you won this round")
        return(1)
    else:
        return(3)
while(cpoint<3 and hpoint<3):
    comp=random.randint(1,3)
    print("ROUND",t)
    print("TOTAL CHANCE LEFT=",t)
    c=input("Enter your choise- \nStone (s) \nPaper (p) \nScissor (k)\n")
    if(c=="s" or c=="p" or c=="k"):
        print("game begins")
    else:
        print("select the write choice")
    q=neutral(comp)
    print("COMPUTER CHOOSED- ",q)
    c=game(c,q)
    if(c==0):
        t=t-1
        F=F+1
        cpoint=cpoint+1
    elif(c==1):
        t=t-1
        F=F+1
        hpoint=hpoint+1
    else:
        print("IT'S A TIE")
    print("COMPUTER POINTS=",cpoint)
    print(" YOUR POINT'S=",hpoint)
if(cpoint==3):
    print(f"COMPUTER WON THE GAME WITH  {cpoint-hpoint} POINTS")
else:
    print(f"YOU WON WITH  {hpoint-cpoint} POINTS")
