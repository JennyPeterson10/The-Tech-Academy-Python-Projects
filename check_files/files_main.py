from tkinter import *
import tkinter as tk


import files_gui
import files_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,200) #(Height, Width)
        self.master.maxsize(500,200)
        # This CenterWindow method will center our app on the user's screen
        files_func.center_window(self,500,200)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: files_func.quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        files_gui.load_gui(self)
        

        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
