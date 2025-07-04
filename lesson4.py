from tkinter import *
import calendar
root=Tk()
#title maker
root.title("cal1")
#giving dimensions to my window
root.geometry("800x800")
#to change background colour
root.config(background="white")

def cal():
    window=Tk()
    window.config(background="white")
    window.title("cal2")
    window.geometry("800x800")
    year1=int(entry.get())
    cal11=calendar.calendar(year1)

    calen4=Text(window,font=("consolas",10),wrap=WORD)
    calen4.insert(1.0,cal11)
    calen4.pack(expand=True,fill=BOTH)
    window.mainloop()


title=Label(root,text="calender",font=("Blackadder ITC",60,"bold"),bg="white")
title.place(x=50,y=50)

year=Label(root,text="type in a year",font=("Blackadder ITC",30,"bold"),bg="white")
year.place(x=50,y=150)

entry=Entry(root,width=30,font=("Blackadder ITC",30,"bold"),bg="white")
entry.place(x=260,y=150)

calender=Button(root,text="calender",font=("Blackadder ITC",30,"bold"),bg="white",bd="4",command=cal)
calender.place(x=100,y=220)

exi=Button(root,text="exit",font=("Blackadder ITC",30,"bold"),bg="white",bd="4",command=exit)
exi.place(x=100,y=320)

root.mainloop()