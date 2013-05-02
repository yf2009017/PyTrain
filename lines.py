from tkinter import Tk,Frame,Label,Button, PhotoImage, Menu
from tkinter import Frame,Label,Entry,Button,TOP,LEFT,RIGHT,END,BOTTOM
from tkinter.messagebox import showinfo
import driver
import stops

class lines(Frame):
    def __init__(self, master=None, bg='black', height=1000, width=1000):
        Frame.__init__(self, master, bg='black', height=1000, width=1000)
        #self.title("CTA Train Tracker ")
        self.driv = driver.Driver()
        self.pack()
        self.memory=''
        lines.make_widgets(self)

    def make_widgets(self):
        self.lines = ['Red Line', 'Blue Line', 'Brown Line', 'Purple Line',
                 'Orange Line', 'Green Line', 'Pink Line', 'Yellow Line']

        headimg = PhotoImage(file='header.gif')
        header = Label(self, image=headimg)
        header.image = headimg
        header.grid(row=0, columnspan=2)
        
        r = 1
        c = 0
        for b in self.lines:
            rel = 'ridge'
            cmd = lambda x=b: self.click(x)
            splt = b.split()
            if splt[0] not in 'OrangeGreenPinkYellow':
                Button(self,text=b, width = 19, height=2, relief=rel,
                       bg = splt[0], fg = "#FFF", font = ("Helvetica", 16),
                       command=cmd).grid(row=r,column=c)
            else:
                Button(self,text=b, width = 19, relief=rel,
                       bg = splt[0], fg = "#000", height=2, font = ("Helvetica", 16),
                       command=cmd).grid(row=r,column=c) 
            c += 1
            if c > 1:
                c = 0
                r += 1
        
    def hello():
            print('hello')    

    def click(self, key):
        for line in self.lines:
            if key == str(line):
                x = self.driv.stopSelection(key)
                stops.stops(x, key).maxsize(480, 320)

myapp = lines()

#
# here are method calls to the window manager class
#
myapp.master.title("CTA Train Tracker")
myapp.master.maxsize(480, 320)

# start the program
myapp.mainloop()
