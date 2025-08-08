from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("lesson5")

root.config(background="white")



title=Label(root,text="mathmantical table",font=("Blackadder ITC",20,"bold"))
title.grid(row=0,column=0)

mr=Label(root,text="number and range",font=("Blackadder ITC",20,"bold"))
mr.grid(row=1,column=0)

num=IntVar()
en=Combobox(root,textvariable=num,width=6)
en["values"]=tuple(range(1,100))
en.grid(row=1,column=1)

num2=IntVar()
rd1=Radiobutton(root,text="10",variable=num2,value=10)

rd2=Radiobutton(root,text="20",variable=num2,value=20)

rd3=Radiobutton(root,text="100",variable=num2,value=100)
rd1.grid(row=1,column=2)
rd3.grid(row=3,column=2)
rd2.grid(row=2,column=2)
ttle=Button(root,text="generate")
ttle.grid(row=2,column=1)

root.mainloop()