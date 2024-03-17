import tkinter as tk
from tkinter import ttk
from res.data import variables, text
from res.Functions import *

class RepitedCombination:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer']) 
        self.root.geometry(variables['size'])
        self.root.resizable(0,0)
        self.data = data

        # Frame
        frame = tk.Frame(self.root)
        frame.pack()
        
        label_m = tk.Label(frame, text=text["total_poblation"], font=("Arial", 20))
        label_n = tk.Label(frame, text=text["selected_poblation"], font=("Arial", 20))
        
        listbox_m = tk.Listbox(frame, width=20, height=5)
        listbox_n = tk.Listbox(frame, width=20, height=5)
        for i in range(1001):
            listbox_m.insert(tk.END, str(i))
            listbox_n.insert(tk.END, str(i))
            
        label_m.grid(row=0, column=0, padx=10, pady=10)
        listbox_m.grid(row=1, column=0, padx=10, pady=10)
        label_n.grid(row=2, column=0, padx=10, pady=10)
        listbox_n.grid(row=3, column=0, padx=10, pady=10)
    
    def run(self):
        self.root.mainloop()
        
    def stop(self):
        self.root.destroy()