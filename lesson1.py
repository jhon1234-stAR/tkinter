from tkinter import *
root=Tk()
#title maker
root.title("starter")
#giving dimensions to my window
root.geometry("800x800")
#to change background colour
root.config(background="blue")

#geomatry mangers for placements pack-will always be in a stack place-take x and y pos
#grit fowlows the grid method by row1 and row 2 so it will change to that pos on the grid

#creating a label diget
#need to use root or your windinow at the start
#login label
lpage=Label(root,text="login page",font=("Blackadder ITC",50,"bold"),bg="blue")
#POS OF LABEL
lpage.place(x=50,y=50)

#username label
username=Label(root,text="username",font=("Blackadder ITC",30,"bold"),bg="blue")
username.place(x=70,y=150)


#password label
pasword=Label(root,text="password",font=("Blackadder ITC",30,"bold"),bg="blue")
pasword.place(x=70,y=240)

#entry box for info

#usermane entry
username2=Entry(root,width=30,font=("Blackadder ITC",30,"bold"),bg="blue")
username2.place(x=240,y=150)

#pasword entry
pasword1=Entry(root,show="*",width=30,font=("Blackadder ITC",30,"bold"),bg="blue")
pasword1.place(x=240,y=240)

#button to enter
button=Button(root,text="enter",font=("Blackadder ITC",30,"bold"),bg="grey",bd="4",relief=RAISED)
button.place(x=240,y=300)

def pasword():
    pasword1.config(show="" if var.get() else "*")
#checkvutton
var=BooleanVar()
Checkbutton(root,text="show pasword",variable=var,bg="blue",command=pasword).place(x=350,y=300)


#end always
mainloop()
