from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("tic tac to")

result=''
turn=1

def win():
    global result
    if (b1.cget('text') == b2.cget('text')==b3.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b1.cget('text')==b2.cget('text')==b3.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b4.cget('text')==b5.cget('text')==b6.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b4.cget('text')==b5.cget('text')==b6.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b7.cget('text')==b8.cget('text')==b9.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b7.cget('text')==b8.cget('text')==b9.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b1.cget('text')==b4.cget('text')==b7.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b1.cget('text')==b4.cget('text')==b7.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b2.cget('text')==b5.cget('text')==b8.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b2.cget('text')==b5.cget('text')==b8.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b3.cget('text')==b6.cget('text')==b9.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b3.cget('text'),b6.cget('text'),b9.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b1.cget('text')==b5.cget('text')==b9.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b1.cget('text')==b5.cget('text')==b9.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b3.cget('text')==b5.cget('text')==b7.cget('text') == 'x'):
        result='player 1 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()
    elif (b3.cget('text')==b5.cget('text')==b7.cget('text') == 'o'):
        result='player 2 wins'
        messagebox.showinfo('results',str(result))
        root.destroy()

def button11():
    global turn
    mytext=b1.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b1.configure(text='x')
            turn=2
            
        else:
            b1.configure(text='o')
            turn=1
    LBL.configure(text='player'+str(turn)+'turns')
    win()

def button21():
    global turn
    mytext=b2.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b2.configure(text='x')
            turn=2
            
        else:
            b2.configure(text='o')
            turn=1
    LBL.configure(text='player'+str(turn)+'turns')
    win()   
def button31():
    global turn
    mytext=b3.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b3.configure(text='x')
            turn=2
            
        else:
            b3.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()

def button41():
    global turn
    mytext=b4.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b4.configure(text='x')
            turn=2
            
        else:
            b4.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()

def button51():
    global turn
    mytext=b5.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b5.configure(text='x')
            turn=2
            
        else:
            b5.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()
def button61():
    global turn
    mytext=b6.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b6.configure(text='x')
            turn=2
            
        else:
            b6.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()
def button71():
    global turn
    mytext=b7.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b7.configure(text='x')
            turn=2
            
        else:
            b7.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()

def button81():
    global turn
    mytext=b8.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b8.configure(text='x')
            turn=2
            
        else:
            b8.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()

def button91():
    global turn
    mytext=b9.cget('text')
    if (mytext == ''):
        if (turn == 1):
            b9.configure(text='x')
            turn=2
            
        else:
            b9.configure(text='o')
            turn=1 
    LBL.configure(text='player'+str(turn)+'turns')
    win()

b1=Button(root,text='',width=5,command=button11)
b1.grid(row=0,column=0,padx=5,pady=5)
b2=Button(root,text='',width=5,command=button21)
b2.grid(row=0,column=1,padx=5,pady=5)
b3=Button(root,text='',width=5,command=button31)
b3.grid(row=0,column=2,padx=5,pady=5)
b4=Button(root,text='',width=5,command=button41)
b4.grid(row=1,column=0,padx=5,pady=5)
b5=Button(root,text='',width=5,command=button51)
b5.grid(row=1,column=1,padx=5,pady=5)
b6=Button(root,text='',width=5,command=button61)
b6.grid(row=1,column=2,padx=5,pady=5)
b7=Button(root,text='',width=5,command=button71)
b7.grid(row=2,column=0,padx=5,pady=5)
b8=Button(root,text='',width=5,command=button81)
b8.grid(row=2,column=1,padx=5,pady=5)
b9=Button(root,text='',width=5,command=button91)
b9.grid(row=2,column=2,padx=5,pady=5)

LBL=Label(root,text='player'+str(turn)+'turns')
LBL.grid(row=10,column=1,padx=5,pady=5)

root.mainloop()