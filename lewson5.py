from tkinter import *
root=Tk()
root.title("lesson5")
root.geometry("800x800")
root.config(background="white")


def al():
    gtk=int(kg.get())*1000

    ptk=int(kg.get())*2.2

    otk=int(kg.get())*35.27

    gr.delete("1.0",END)
    gr.insert(END,gtk)

    p.delete("1.0",END)
    p.insert(END,ptk)

    o.delete("1.0",END)
    o.insert(END,otk)













title=Label(root,text="enter the weight in kilograms",font=("Blackadder ITC",20,"bold"),bg="white")
title.grid(row=0,column=0)

kg=Entry(root,font=("Blackadder ITC",20,"bold"),bg="white",bd=4)
kg.grid(row=0,column=1)

con=Button(root,text="convert",font=("Blackadder ITC",20,"bold"),bg="grey",bd=3,command=al)
con.grid(row=0,column=2)

gl=Label(root,text="grams",font=("Blackadder ITC",20,"bold"),bg="white")
gl.grid(row=2,column=0)

pl=Label(root,text="pounds",font=("Blackadder ITC",20,"bold"),bg="white")
pl.grid(row=2,column=1)

ol=Label(root,text="ounses",font=("Blackadder ITC",20,"bold"),bg="white")
ol.grid(row=2,column=2)

gr=Text(root,height=1,width=20)
gr.grid(row=3,column=0)

p=Text(root,height=1,width=20)
p.grid(row=3,column=1)

o=Text(root,height=1,width=20)
o.grid(row=3,column=2)

root.mainloop()