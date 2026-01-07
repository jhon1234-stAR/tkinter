from tkinter import *
from tkinter.colorchooser import askcolour
root=Tk()
root.title("colour painter ")###chand eraser to earaser at the end

class paint(object):
    DEFULT_PENSIZE=5.0
    DEFULT_COLOUR="black"
    def __init__(self):
        self.root=Tk()

        self.pen_Button=Button(self.root,text="pen",command=self.use_pen)
        self.pen_Button.grid(row=0,column=0,padx=5,pady=5)

        self.brush_Button=Button(self.root,text="brush",command=self.use_brush)
        self.brush_Button.grid(row=1,column=0,padx=5,pady=5)

        self.colour_Button=Button(self.root,text="colour",command=self.use_colour)
        self.colour_Button.grid(row=2,column=0,padx=5,pady=5)

        self.eraser_Button=Button(self.root,text="eraser",command=self.use_eraser)
        self.eraser_Button.grid(row=3,column=0,padx=5,pady=5)

        self.scale_Button=Scale(self.root,from_=1,to=10)
        self.scale_Button.grid(row=4,column=1,padx=5,pady=5)

        self.c=Canvas(self.root,bg="white",width=600,height=600)
        self.c.grid(row=5,column=0,padx=5,pady=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x=None
        self=None
        self.line_width=self.choose_size_button.get()
        self.colour=self.DEFULT_COLOUR
        self.eraser_on=False
        self.activate_button=self.pen_button
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<buttonRealease-1>',self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)
    def use_brush(self):
        self.activate_button(self.brush_button)
    def choose_colour(self):
        self.eraser_on=False
        self.colour=askcolour(colour=self.colour)[1]
    def use_eraser(self):
        self.activate_button(self.eraser_button,eraser_mode=True)
    def activate_button(self,some_button,eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.activate_button=some_button
        self.eraser_on=eraser_mode
        

    def paint(self,event):
        self.line_width=self.choose_size_button.get()
        paint_colour='white' if self.eraser_on else self.colour
        if self.old_x and self_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y
                               width=self.line_width,fill=paint_colour,capstyle=ROUND,
                               smooth=True,splinestep=36)
            self.old_x=event.x
            self.old_y=event.y
            def reset(self,event):
                self.old_x,self.old_y=None,None

if __name__ == "__main__":
    paint()


root.mainloop()