from tkinter import *
root=Tk()
root.title("lesson2")
root.geometry("800x800")
root.config(background="white")

l1=Label(root,text="sweets and choclate",font=("Blackadder ITC",50,"bold"))
l1.pack()

f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack()

b1f1=Button(f1,text="dark chocolate",bg="black",fg="white")
b1f1.pack(side=LEFT)
b2f1=Button(f1,text="milk chocolate",bg="brown")
b2f1.pack(side=LEFT)
b3f1=Button(f1,text="white chocolate",bg="white")
b3f1.pack(side=LEFT)








root.mainloop()

