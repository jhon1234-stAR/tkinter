from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.dialog import *
import speech_recognition as sr
root=Tk()
root.title(" ")
root.config(background="black")
root.geometry(800,400)




heading1=Label(root,text="voice notepad ",font=("Blackadder ITC",20,"bold"))
heading1.grid(row=0,column=0,pady=20,padx=20)

label1=Label(root,text="click button to record you speach",font=("Blackadder ITC",20,"bold"))
label1.grid(row=1,column=0,pady=20,padx=20)

output_text=Text(root,hight=4,width=40)
output_text.grid(row=1,column=1,pady=20,padx=20)

def translate():
    r=sr.Recognizer()
    with sr.Microphone() as sourse:
        print("say anything")
        audio=r.listen(sourse)
        try:
            text=r.recognise_google(audio)
        except:
            text="sorry could not unerstand you voice"
        output_text.delete(1,0,END)
        output_text.insert(END,text)



root.mainloop()