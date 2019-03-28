# Created by Jenny Peterson March 27, 2019

from tkinter import *
import tkinter as tk

import files_main
import files_func



def load_gui(self):

    # Define buttons
    self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=W)
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_check.grid(row=2,column=0,rowspan=2,padx=(20,0),pady=(10,0),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=2,column=2,rowspan=2,padx=(20,0),pady=(10,0),sticky=E)



    # Define browse fields
    self.txt_browse = tk.Entry(self.master,text='',width=55)
    self.txt_browse.grid(row=0,column=1,rowspan=1,columnspan=2,padx=(20,0),pady=(40,0),sticky=E+W)
    self.txt_browse2 = tk.Entry(self.master,text='',width=55)
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=2,padx=(20,0),pady=(10,0),sticky=E+W)




if __name__ == "__main__":
    pass
