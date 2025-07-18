from tkinter import *
root=Tk()
root.title("lesson5")
root.geometry("800x800")
root.config(background="white")

def al():
    gtk=(int(kg.get())*1.8)+32

    gr.delete("1.0",END)
    gr.insert(END,gtk)



title=Label(root,text="enter celcilus",font=("Blackadder ITC",20,"bold"),bg="white")
title.grid(row=0,column=0)

kg=Entry(root,font=("Blackadder ITC",20,"bold"),bg="white",bd=4)
kg.grid(row=0,column=1)


con=Button(root,text="convert",font=("Blackadder ITC",20,"bold"),bg="grey",bd=3,command=al)
con.grid(row=0,column=2)



gl=Label(root,text="farenhight",font=("Blackadder ITC",20,"bold"),bg="white")
gl.grid(row=2,column=0)

gr=Text(root,height=1,width=20)
gr.grid(row=3,column=0)


root.mainloop()