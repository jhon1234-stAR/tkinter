from tkinter import *
root=Tk()
root.title("lesson5")
root.geometry("800x800")
root.config(background="white")



title=Label(root,text="rock paper sizzors shoot",font=("Blackadder ITC",30,"bold"),bg="white")
title.pack()

start=Label(root,text="lets start the game",font=("Blackadder ITC",20,"bold"),bg="white")
start.pack(pady=10)

f1=Frame(root,bg="white")
f1.pack()
op=Label(f1,text="options here:",font=("Blackadder ITC",25,"bold"),bg="light blue")
op.grid(row=0,column=0)

con=Button(f1,text="rock",font=("Blackadder ITC",25,"bold"),bg="pink",bd=3,)
con.grid(row=1,column=0)
con=Button(f1,text="paper",font=("Blackadder ITC",25,"bold"),bg="light blue",bd=3,)
con.grid(row=1,column=1)
con=Button(f1,text="sizzors",font=("Blackadder ITC",25,"bold"),bg="pink",bd=3,)
con.grid(row=1,column=2,padx=10)

o=Label(f1,text="score:",font=("Blackadder ITC",25,"bold"),bg="pink")
o.grid(row=3,column=0,pady=15)


ol=Label(f1,text="your score:",font=("Blackadder ITC",25,"bold"),bg="pink")
ol.grid(row=4,column=1,pady=15)

os=Label(f1,text="your answer:",font=("Blackadder ITC",25,"bold"),bg="pink")
os.grid(row=4,column=0,padx=20)


oc=Label(f1,text="computers answer:",font=("Blackadder ITC",25,"bold"),bg="pink")
oc.grid(row=5,column=0,pady=16)


oc2=Label(f1,text="computers score:",font=("Blackadder ITC",25,"bold"),bg="pink")
o.grid(row=5,column=1)

root.mainloop()