# Created by Jenny Peterson March 29, 2019

from tkinter import *
import tkinter as tk


import folder_main
import folder_func



def load_gui(self):

    # Define button and label
    self.btn_browse = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: folder_func.openDir(self))
    self.btn_browse.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=W)
    self.lbl_directory = tk.Label(self.master,width=15,height=1,text='Selected Directory: ')
    self.lbl_directory.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=W)


    # Define text field
    self.txt_browse = tk.Entry(self.master,text='',width=55)
    self.txt_browse.grid(row=1,column=1,padx=(20,0),pady=(10,0),sticky=E+W)



if __name__ == "__main__":
    pass
