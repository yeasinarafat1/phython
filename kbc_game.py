import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
questions= [
    ["In which year phython was first released","1978","1980","1991","1990",3],
    ["Who developed phython ?", "Mark","Elon","Borhan","van rusem",4],
    ["What is the phython latest version?","3.6.0","3.10.5","3.5.0","3.7.7",2]
    
]
level = [1000,2000,5000,10000,20000,50000,100000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    heading = f"You are playing for BDT {level[i]}"
    print(heading)
    speak.speak(heading)
    q =f"Your question is : {question[0]}" 
    print(q)
    speak.speak(q)
    time.sleep(1)
    o1 = f"option 1 {question[1]}          option 2 {question[2]}"
    print(f"1.{question[1]}          2.{question[2]}")
    speak.speak(o1)
    time.sleep(1)
    o2 = f"option 3 {question[3]}          option 4 {question[4]}"
    print(f"3.{question[3]}          4.{question[4]}")
    speak.speak(o2)
    reply = int(input("Enter your ans: "))
    if(reply==question[-1]):
        print("Corect Answers")
        print(f"You won BDT{level[i]}")
        money = level[i]
        f=f"corect answer you have won {level[i]} taka "
        speak.speak(f)
    else:
        print("Wrong Answer")
        t = "wrong answer you have lost the game "
        speak.speak(t)

        break
print(f"Game over you have won BDT{money} ")
r = f"Game over you have won BDT{money} "
speak.speak(r)
