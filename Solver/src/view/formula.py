import tkinter as tk
from tkinter import ttk
from res.data import variables, text, formula_desc
from res.Functions import *

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
        label1_text = text["formula_is"] +  TypeOperation(self.format_data())
        
        # Label for the formula
        label2_formula = formula_desc[TypeOperation(self.format_data())]
        
        label1 = tk.Label(frame, text=label1_text)
        label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        label2 = tk.Label(frame, text=label2_formula)
        label2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
    def format_data(self):
        return (value for value in self.data.values())
    
    def run(self):
        self.root.mainloop()
        
    def stop(self):
        self.root.destroy()
