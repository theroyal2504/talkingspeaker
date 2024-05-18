#pls pip  install pypiwin32
from win32com.client import Dispatch
print("Wellcome to Speak")
print("NOTE :- enjoy in program and  exit to press Z key to enter \n Thankyou")
while True:
    x = input("Enter what you want to me to speak:   ")
    speak = Dispatch("SAPI.SpVoice").Speak
    if x == "z":
        speak("Nice to meet u thankyou by sir")
        break
    speak(x)
print("by by")