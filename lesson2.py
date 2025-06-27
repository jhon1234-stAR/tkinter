#we are doing work n the menu bar today of vs code
from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("lesson2")
root.geometry("800x800")
root.config(background="white")
#menu main part
menubar=Menu(root)


def bar():
    import time
    progress["value"]=20
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=40
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=60
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=80
    root.update_idletasks()
    time.sleep(1)
    progress["value"]=100







#first small one of of menu the file  menu on the second part of the thing has to be in caps
m1=Menu(menubar,tearoff=0)
#first option for the menu with cacade effect so when you click on it you wil go down for
#  more info
menubar.add_cascade(label="file",menu=m1)
#makig the cacading things to go dounw nnwehn you click them 
#new file
m1.add_cascade(label="new file")
#new folder
m1.add_cascade(label="new new folder")
#new window
m1.add_cascade(label="new window")

#seperator
m1.add_separator()
#open file
m1.add_cascade(label="open file")
#open folder
m1.add_cascade(label="open folder")
#seperator
m1.add_separator()
#save
m1.add_cascade(label="save")
#save as
m1.add_cascade(label="save as")
#save all
m1.add_cascade(label="save all")
#separator
m1.add_separator()
#exit
m1.add_cascade(label="exit",command=root.destroy)

#doing the same for all the oher options
#eddit
#starter
m2=Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=m2)
#extra 
m2.add_cascade(label="undo")
m2.add_cascade(label="redo")

m2.add_separator()

m2.add_cascade(label="cut")
m2.add_cascade(label="copy")
m2.add_cascade(label="paste")

m2.add_separator()

m2.add_cascade(label="find file")
m2.add_cascade(label="replace file")

m2.add_separator()

m2.add_cascade(label="exit",command=root.destroy)
#making a bar with a start laoder
m3=Menu(menubar,tearoff=0)
menubar.add_cascade(label="start",menu=m3)
#only label
m3.add_command(label="progress",command=bar)

m3.add_command(label="spin box",command=bar)


progress=Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")
progress.pack(pady=100)
    
b=Spinbox(root,from_=0,to=100)
b.pack(pady=25)

#run code
root.config(menu=menubar)
mainloop()






