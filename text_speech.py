import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

while True:    
    text = input("Enter what you want to say: ")  
    speak.Speak(text)
    if(text=="q"):
        speak.Speak("Program closed")
        break