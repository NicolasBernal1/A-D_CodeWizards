import tkinter as tk
from tkinter import ttk
from res.data import variables
from res.Functions import *

class OrdinaryVariation:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer']) 
        self.root.geometry(variables['size'])
        self.root.resizable(0,0)
        self.data = data

        # Frame
        frame = tk.Frame(self.root)
        frame.pack()
    
    def run(self):
        self.root.mainloop()
        
    def stop(self):
        self.root.destroy()