from tkinter import * 
from time import strftime
root=Tk()
root.title("lesson5")



def times():
    time=strftime("%H:%M:%S %p")
    title.config(text=time)
    title.after(1000,times)



title=Label(root,font=("Blackadder ITC",30,"bold"))
title.pack()
times()

mainloop()