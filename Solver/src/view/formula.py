import tkinter as tk
from tkinter import ttk
from res.data import variables, text

class Formula:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer']) 
        self.root.geometry(variables['size'])
        self.root.resizable(0,0)
        self.data = data

        # Frame
        frame = tk.Frame(self.root)
        frame.pack()
        
        # Identificate the formula
        text = "The formula is [BURNED CODE]"
        
        # Label for the formula
        
        label = tk.Label(frame, text=text)
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        

    def run(self):
        self.root.mainloop()
        
    def stop(self):
        self.root.destroy()
