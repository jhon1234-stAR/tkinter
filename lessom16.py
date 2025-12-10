
import tkinter
from tkinter import *
import random

from tkinter import messagebox
root=Tk()
score=0

answers=["Supercalifragilisticexpialidocious","Abhor ","Alacrity ","apple","Lugubrious ","hard","long","eight","love","drop","confused","Obsequious ","clever","happy","Antithesis ","hi","bye","luck","unluck","twenty","five"]

words=["Sioisactfaeauxcrlglulieirpdioipics ","Aobhr ","Aitrcaly ","papel","Lgobuuruis ","ardh","onlg","igeth","ovle","ordp","cdesufon","rcvlee","hapyp","iahenttiss","ih","ybe","ulkc","ulukcn","wetnyt","ivef"]



num=random.randrange(0,len(words),1)
c=0
d=0
s=""
l=Label(root)

def reset():
    global num, answers, words
    num=random.randrange(0,len(words),1)
    heading1.config(text=words[num])
    e1.delete(0,END)

def defult():
    global num, answers, words
    heading1.config(text=words[num])


def checkans():
    global num, answers, words, s ,l , d, c
    d=int(d)+1
    var=e1.get()
    if var == answers[num]:
        messagebox.showinfo("yay you did it")
        c=int(c)+1
        s="score :"+str(c)+"/"+str(d)
        
    else:
        messagebox.showinfo("oh no you failed in like ha imagine")
        s="score :"+str(c)+"/"+str(d)
    l.forget()
    l=Label(root,text=s)
    l.pack(side=CENTER)
    reset()



root.title("jumbled word game")
root.configure(background="hot pink")




word=Label(root,text="jumbled word game")
word.grid(row=0,column=0,pady=20,padx=20)

heading1=Label(root,text="not working rn srry")
heading1.grid(row=1,column=1,pady=20,padx=20)


d1=Button(root,text="check ans",command=checkans)
d1.grid(pady=40,padx=5,row=6,column=1)
ans=StringVar()
e1=Entry(root,textvariable=ans)
e1.grid(row=3,column=1,pady=20,padx=20)

reset1=Button(root,text="reset",command=reset)
reset1.grid(row=4,column=1,pady=20,padx=20)


word=Label(root,text=score)
word.grid(row=5,column=0,pady=20,padx=20)

defult()

root.mainloop()