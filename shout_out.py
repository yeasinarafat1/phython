import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")
# time.sleep(2)
# text = "I read in CPI"
# speak.Speak(text)

# # 3 second sleep
# time.sleep(1) 

# text = "I am studing diploma in engineering"
# speak.Speak(text)
while True:
    Name = str(input("Enter your name: "))
    
    text = f"My name is {Name}. I read in CPI"
    speak.Speak(text)
import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

    
text = "Borhan is a motherfucker"    
speak.Speak(text)