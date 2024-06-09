# main.py
import tkinter as tk

from framehome import Frame_Home
from framerule import Frame_Rule
from frame0 import Frame_0
from frame1 import Frame_1
from frame2 import Frame_2
from frame3 import Frame_3
from framemusic import Frame_Music
from getdata import GetData  # add

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("400x300")  # ウィンドウのサイズを指定
        self.resizable(False, False)  # ウィンドウのリサイズを無効にする

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.framehome =Frame_Home(master=self)
        self.framerule = Frame_Rule(master=self)
        self.frame0 = Frame_0(master=self)
        self.frame1 = Frame_1(master=self)
        self.frame2 = Frame_2(master=self)
        self.frame3 = Frame_3(master=self)
        self.framemusic = Frame_Music(master=self)

        self.framehome.grid(row=0, column=0, sticky="nsew")
        self.framerule.grid(row=0, column=0, sticky="nsew")
        self.frame0.grid(row=0, column=0, sticky="nsew")
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=0, sticky="nsew")
        self.frame3.grid(row=0, column=0, sticky="nsew")
        self.framemusic.grid(row=0, column=0, sticky="nsew")

        self.framehome.tkraise()

        self.data = GetData() # add

if __name__=="__main__":
    app = App()
    app.mainloop()
