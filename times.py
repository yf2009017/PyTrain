from tkinter import Tk,Frame,Label,Button, Toplevel, PhotoImage, Menu
from calendar import monthrange
from tkinter.simpledialog import askstring
from tkinter import Frame,Label,Entry,Button,TOP,LEFT,RIGHT,END,BOTTOM
from tkinter.messagebox import showinfo
import driver

class times(Toplevel):
    def __init__(self, trains, time, stop, master=None):
        Toplevel.__init__(self, master, bg='black')
        #self.title("CTA Train Tracker ")
        self.driv = driver.Driver()
        self.tra = trains
        self.tim = time
        self.stop = stop
        times.make_widgets(self)

    def make_widgets(self):
        timeimg = PhotoImage(file='times.gif')
        timer = Label(self, image=timeimg)
        timer.image = timeimg
        timer.grid(row=0, columnspan=2)

        
        
        r = 1
        c = 0
        for i in range(0, len(self.tim)):
            colors = {'Red':'red', 'Blu':'blue', 'Brn':'brown', 'Pur':'purple',
                      'Org':'orange', 'Grn':'Green', 'Pnk':'pink', 'Yel':'yellow'}
            splt = self.tra[i].split()    
            if splt[0] not in 'OrgGrnPnkYel':
                Label(self, text=("{0:8}".format(self.tra[i])),
                      font=("Helvetica", 12), width=20, bg=colors[splt[0]],
                      fg="#FFF").grid(row=r,column=c)
                Label(self, text=("{0:5}".format(self.tim[i])),
                      font=("Helvetica", 12), width=10, bg=colors[splt[0]],
                      fg="#FFF").grid(row=r,column=c+1)
            else:
                Label(self, text=("{0:8}".format(self.tra[i])),
                      font=("Helvetica", 12), width=20, bg=colors[splt[0]],
                      fg="#000").grid(row=r,column=c)
                Label(self, text=("{0:5}".format(self.tim[i])),
                      font=("Helvetica", 12), width=10, bg=colors[splt[0]],
                      fg="#000").grid(row=r,column=c+1)
            c += 1
            if c > 0:
                c = 0
                r += 1

        Button(self, text="< Back", width = 5, relief='ridge',
                       bg = "#000", fg = "#FFF", font = "Helvetica",
                       command=self.destroy).grid(row=r,columnspan=2)
