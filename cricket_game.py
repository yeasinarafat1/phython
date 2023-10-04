''' Game rules first you have tose head or tell if toss is your chossen number than you will bat first 
 otherwise computer will bat first'''
''' In bating mode you have to chosse a number if your chossen numbeer and computer choosen number are same
 than you are out otherwise your scoreboard will extend acording to your choosen number '''
'''In boaling mode you have to choose a number between 1-6 if your choosen number is same as computer choosen number 
then computer will be out otherwise computer scoreboard will extend'''
import random
toss = int(input("Enter 1 for head and 2 for tell : "))
toss_  = random.randint(1,2)
if(toss==toss_):
    user_score = 0
    comp_score = 0
    print("You have won the toss now your bating")
    for i in range(0,1000):
        user = int(input("Enter your number between 1-6: "))
        comp = random.randint(1,6)
    # user_score = 0
        if(user==comp):
            print("You are out!")
            print(f"You scored {user_score} run")
            print(f"Computer has to score {user_score + 1} run to win")
            break
        else:
            user_score = user_score + user
            print(f"You have scored {user} run")
            print(f"Total score {user_score}")
    for i in range(1,1000):
        user = int(input("Enter your number between 1-6: "))
        comp = random.randint(1,6)
        comp_score = comp_score + comp
        if(user==comp and comp_score==user_score):
            comp_score = comp_score-comp
            print("Match Draw!")
            break
        elif(user==comp):
            print(f"computer is out and scored {comp_score} run")
            print(f"You have won the game by {user_score - comp_score} run")
            comp_score = comp_score - comp
            break
        elif(comp_score>user_score):
            #  comp_score = comp_score+ comp
             print(f"computer has scored {comp} run")
             print("computer has won the game")
             print("Better luck next time")
             break
        else:
            # comp_score = comp_score + comp
            print(f"computer has scored {comp} run")
            print(f"Total score is {comp_score}")
            print(f"computer has to score {user_score-comp_score} runs to win")
else:
    user_score = 0
    comp_score = 0
    print("you have lost toss")
    print("Computer will bat first")
    for i in range(0,1000):
        user = int(input("Enter your number between 1-6: "))
        comp = random.randint(1,6)
    # user_score = 0
        if(user==comp):
            print("Computer is out!")
            print(f"Computer scored {comp_score} run")
            print(f"You have to score {comp_score + 1} run to win")
            break
        else:
            comp_score = comp_score + comp
            print(f"Computer has scored {comp} run")
            print(f"Total score {comp_score}")
    for i in range(0,1000):
        user = int(input("Enter your number between 1-6: "))
        comp = random.randint(1,6)
        user_score = user_score + user
        if(user==comp and user_score == comp_score):
           user_score = user_score - user
           print("Match Draw!")
           break
        elif(user==comp and user_score==comp_score):
             user_score = user_score - user
             print(f"You are out! and scored {user_score} run")
             print(f"computer has won the game by {comp_score - user_score} run")
             print("Final sumury")
             print(f"You have scored {user_score} run")
             print(f"Computer has scored {comp_score} run")
             break
        elif(user_score==comp_score+1 or user_score>comp_score):
            #  user_score = user_score + user
             print(f"You have scored {user} run")
             print("congratulation............!")
             print("You have  won the game")
             break
        else:
            # user_score = user_score + user
            print(f"You have scored {user} run")
            print(f"Total score is {user_score}")
            print(f"You have to score {comp_score-user_score} to win")
        
        
        
    

