from tkinter import Tk,Frame,Label,Button
from calendar import monthrange
from tkinter.simpledialog import askstring
from tkinter import Frame,Label,Entry,Button,TOP,LEFT,RIGHT,END,BOTTOM
from tkinter.messagebox import showinfo
import driver, lines, stops

class traintracker(Frame):
    def __init__(self, bg='black', parent=None):
        Frame.__init__(self, bg='black', parent=None)
        #self.title("CTA Train Tracker ")
        self.driv = driver.Driver()
        self.pack()
        self.memory=''
        traintracker.make_widgets(self)

    def make_widgets(self):
        lines.lines().mainloop()
