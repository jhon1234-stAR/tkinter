from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import speech_recognition as sr
root=Tk()
root.title(" ")
root.config(background="black")





heading1=Label(root,text="voice notepad ",)
heading1.grid(row=0,column=0,pady=20,padx=20)

label1=Label(root,text="click button to record you speach",)
label1.grid(row=1,column=0,pady=20,padx=20)

output_text=Text(root,height=4,width=40)
output_text.grid(row=1,column=1,pady=20,padx=20)

def translate():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say anything")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            text="sorry could not unerstand you voice"
        output_text.delete(1.0,END)
        output_text.insert(END,text)

def save():
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        print(output_text.get(1.0,END),file=fout)
    else:
        messagebox.showinfo("WARNING","Text file not saved")
trans_btn=Button(root,text="click on me.. to start recording",command=translate,width=20)
trans_btn.grid(row=2,column=0,pady=20,padx=20)

save_btn=Button(root,text="save text",command=save,width=20)
save_btn.grid(row=1,column=2,pady=20,padx=20)
root.mainloop()