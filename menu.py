from tkinter import *
class App(Frame):


    def __init__(self, master):
            
        """Initialise the base class"""
        Frame.__init__(self,master)

        """Set the Window Title"""
        self.master.title("TkInter Menus")
        self.configure(height=200,width=200)
        """Display the main window
        with a little bit of padding"""
        self.grid(padx=15, pady=15,sticky=N+S+E+W)       

        #Create the Menu base
        self.menu = Menu(self)
        #Add the Menu
        self.master.config(menu=self.menu)
        
        #Create our Python menu
        self.tkMenu = Menu(self.menu)
        #Add our Menu to the Base Menu
        self.menu.add_cascade(label="TkMenu", menu=self.tkMenu)

        #Add items to the menu
        self.tkMenu.add_command(label="Simple", command=self.Simple)
        self.tkMenu.add_separator()
        self.tkMenu.add_command(label="Menu", command=self.Menu)

    def Simple(self):
        self.showinfo("Simple", "Simple")
    def Menu(self):
        self.showinfo("Menu", "Menu")        	


if __name__ == "__main__":
	root = Tk()
	app = App(root)
	root.mainloop()
