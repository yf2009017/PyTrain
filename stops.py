from tkinter import Tk,Frame,Label,Button, Toplevel, PhotoImage, Menu
from calendar import monthrange
from tkinter.simpledialog import askstring
from tkinter import Frame,Label,Entry,Button,TOP,LEFT,RIGHT,END,BOTTOM
from tkinter.messagebox import showinfo
import driver, times

class stops(Toplevel):
    def __init__(self, dictionary, linein, master=None):
        Toplevel.__init__(self, master,  bg='black')
        #self.title("CTA Train Tracker ")
        self.driv = driver.Driver()
        self.linein = linein
        self.line = self.linein.split()
        self.stored = dictionary
        stops.make_widgets(self)

    def make_widgets(self):
        
        stops = self.stored.keys()
        sortedstops = []

        for stop in stops:
            sortedstops.append(stop)
        sortedstops.sort()

        
        stopimg = PhotoImage(file='stop.gif')
        pickstop = Label(self, image=stopimg)
        pickstop.image = stopimg
        pickstop.grid(row=0, columnspan=4)
        r = 1
        c = 0
        
        for stop in sortedstops:
            rel = 'ridge'
            cmd = lambda x=stop: self.click(x)
            if self.line[0] not in 'OrangeGreenPinkYellow':
                Button(self,text=stop, width = 19, relief=rel, fg = "#FFF",
                       bg = self.line[0], font = ("Helvetica", 8),
                       command=cmd).grid(row=r,column=c)
            else:
                Button(self,text=stop, width = 19, relief=rel, fg = "#000",
                       bg = self.line[0], font = ("Helvetica", 8),
                       command=cmd).grid(row=r,column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

        Button(self, text="< Back", width = 5, relief='ridge',
                       bg = "#000", fg = "#FFF", font = "Helvetica",
                       command=self.destroy).grid(row=r+1,columnspan=4)

    def click(self, key):
        stops = self.stored.keys()
        urls = self.stored.values()
        for stop in stops:
            if key == stop:
                tra = self.driv.getTrains(self.stored[key])
                tim = self.driv.getTimes(self.stored[key])
                times.times(tra, tim, key).maxsize(480, 320)
        return

    
