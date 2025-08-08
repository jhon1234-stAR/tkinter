from tkinter import * 
from tkinter import messagebox

import random
root=Tk()
root.title("lesson0")
root.config(background="black")
num=random.randint(1,20


def evil1button():
    my_name_=title.get()
    messagebox.showinfo("evil1",f"hello {my_name_} you have to guese my number from 1 to 20 or there will be consequences smiley face")

def lifechoices():
    
    theirchoice=int(tile.get())
    if theirchoice==num:
        messagebox.showinfo(message=f"well done you have won for now the number was {num}")
    elif theirchoice<num:
        messagebox.showinfo(message="one more desicion go higher")
    elif theirchoice>num:
        messagebox.showinfo(message="one more choice lower")
    


title=Label(root,text="welcome to my evil domain",font=("Blackadder ITC",30,"bold"),bg="black",fg="white")
title.pack()

e=Label(root,text="write your name",font=("Blackadder ITC",30,"bold"),bg="black",fg="white")
e.pack()
title=Entry(root,font=("Blackadder ITC",30,"bold"),bg="white")
title.pack()
tle=Button(root,text="press me or else",font=("Blackadder ITC",30,"bold"),bg="dark red",command=evil1button)
tle.pack()
el=Label(root,text="write the number",font=("Blackadder ITC",30,"bold"),bg="black",fg="white")
el.pack()
tile=Entry(root,font=("Blackadder ITC",30,"bold"),bg="white")
tile.pack()
ttle=Button(root,text="press me or else",font=("Blackadder ITC",30,"bold"),bg="dark red",command=lifechoices)
ttle.pack()



root.mainloop()

















































