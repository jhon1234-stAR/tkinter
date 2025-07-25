from tkinter import * 
import random
root=Tk()
root.title("lesson5")
root.geometry("800x800")
root.config(background="white")
scorep=0
scorec=0
rps=["rock","paper","sizzors"]

def botwins():
    global scorec 
    scorec+=1
    start.config(text="bot wins!!")
    oc2.config(text="computer score:"+str(scorec))
    ol.config(text="your score:"+str(scorep))
def playerwins():
    global scorep
    scorep+=1
    start.config(text="you win!!")
    ol.config(text="your score:"+str(scorep))
    oc2.config(text="computer score:"+str(scorec))

def ties():
    ol.config(text="your score:"+str(scorep))
    start.config(text="tie!!! !!!")
    oc2.config(text="computer score:"+str(scorec))
   

def choicepl(plinput):
    cinput=random.choice(rps)

    os.config(text="your answer: "+plinput)
    oc.config(text="coputers answer: "+cinput)

    if plinput==cinput:
        ties()
    elif plinput=="rock" and cinput=="paper":
        botwins()
    elif plinput=="rock" and cinput=="sizzors":
        playerwins()
    elif plinput=="paper" and cinput=="rock":
        playerwins()
    elif plinput=="paper" and cinput=="sizzors":
        botwins()
    elif plinput=="sizzors" and cinput=="rock":
        botwins()
    elif plinput=="sizzors" and cinput=="paper":
        playerwins()







title=Label(root,text="rock paper sciscors shoot",font=("Blackadder ITC",30,"bold"),bg="white")
title.pack()

start=Label(root,text="lets start the game",font=("Blackadder ITC",20,"bold"),bg="white")
start.pack(pady=10)

f1=Frame(root,bg="white")
f1.pack()
op=Label(f1,text="options here:",font=("Blackadder ITC",25,"bold"),bg="light blue")
op.grid(row=0,column=0)

con=Button(f1,text="rock",font=("Blackadder ITC",25,"bold"),bg="pink",bd=3,command=lambda:choicepl("rock"))
con.grid(row=1,column=0)
con0=Button(f1,text="paper",font=("Blackadder ITC",25,"bold"),bg="light blue",bd=3,command=lambda:choicepl("paper"))
con0.grid(row=1,column=1)
con6=Button(f1,text="sizzors",font=("Blackadder ITC",25,"bold"),bg="pink",bd=3,command=lambda:choicepl("sizzors"))
con6.grid(row=1,column=2,padx=10)

o=Label(f1,text="score:",font=("Blackadder ITC",25,"bold"),bg="pink")
o.grid(row=3,column=0,pady=15)


ol=Label(f1,text="your score:",font=("Blackadder ITC",25,"bold"),bg="pink")
ol.grid(row=4,column=1,pady=15)

os=Label(f1,text="your answer:",font=("Blackadder ITC",25,"bold"),bg="pink")
os.grid(row=4,column=0,padx=20)


oc=Label(f1,text="computers answer:",font=("Blackadder ITC",25,"bold"),bg="pink")
oc.grid(row=5,column=0,pady=16)


oc2=Label(f1,text="computers score:",font=("Blackadder ITC",25,"bold"),bg="pink")
oc2.grid(row=5,column=1)

root.mainloop()