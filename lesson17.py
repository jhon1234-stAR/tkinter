from tkinter import *
from tkinter.colorchooser import askcolor



class Paint:
    DEFAULT_PENSIZE=5.0
    DEFAULT_COLOR="black"
    def __init__(self):
        self.root=Tk()
        self.root.title("paint")
        self.pen_Button=Button(self.root,text="pen",command=self.use_pen)
        self.pen_Button.grid(row=0,column=0,padx=5,pady=5)

        self.brush_Button=Button(self.root,text="brush",command=self.use_brush)
        self.brush_Button.grid(row=1,column=0,padx=5,pady=5)
    

        self.color_Button=Button(self.root,text="color",command=self.choose_color)
        self.color_Button.grid(row=2,column=0,padx=5,pady=5)

        self.eraser_Button=Button(self.root,text="eraser",command=self.use_eraser)
        self.eraser_Button.grid(row=3,column=1,padx=5,pady=5)

        self.scale_Button=Scale(self.root,from_=1,to=10,orient=HORIZONTAL)
        self.scale_Button.set(self.DEFAULT_PENSIZE)
        self.scale_Button.grid(row=4,column=1,padx=5,pady=5)

        self.c=Canvas(self.root,bg="white",width=600,height=600)
        self.c.grid(row=5,column=0,padx=5,pady=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x=None
        self.old_y=None
        
        self.color=self.DEFAULT_COLOR
        self.eraser_on=False
        self.active_button=self.pen_Button
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)

    def use_pen(self):
        self.activate_Button(self.pen_Button)
    def use_brush(self):
        self.activate_Button(self.brush_Button)
    def choose_color(self):
        self.eraser_on=False
        self.color=askcolor(color=self.color)[1]
    def use_eraser(self):
        self.activate_Button(self.eraser_Button,eraser_mode=True)
    def activate_button(self,some_Button,eraser_mode=False):
        self.activate_Button.config(relief=RAISED)
        some_Button.config(relief=SUNKEN)
        self.activate_button=some_Button
        self.eraser_on=eraser_mode
        

    def paint(self,event):
        line_width=self.scale_Button.get()
        paint_color='white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,
                               width=line_width,fill=paint_color,capstyle=ROUND,
                               smooth=True,splinestep=36)
            
        self.old_x=event.x
            
        self.old_y=event.y
    def reset(self,event):
        self.old_x,self.old_y=None,None

if __name__ == "__main__":
    Paint()

