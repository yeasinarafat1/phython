import random
user_win=0
comp_win=0
print("-1 for snake ")
print("0 for water")
print("1 for gun")
for i in range(0,10):
    comp = random.randint(-1,1)
    user = int(input("enter a number between -1 to 1: "))
    if(comp==-1 and user==-1):
        print("you hve won")
        user_win = user_win+1
    elif(comp==0 and user==-1):
        print("You have won")
        user_win = user_win+1
    elif(comp==1 and user==0):
        print("you have won")
        user_win = user_win+1
    elif(comp==-1 and user==0):
        print("you have lost")
        comp_win=comp_win+1
    elif(comp==0 and user==1):
        print("you have lost")
        comp_win=comp_win+1
    elif(comp==1 and user==1):
        print("you have lost")
        comp_win=comp_win+1
    elif(comp==user):
        print("Draw")
    print(f"computer chose {comp} and you chose {user}")
    print(f"you have  {user_win} times")
    print(f"computer have won {comp_win} times")


