import tkinter as tk
from tkinter import ttk
from res.data import variables, text
from res.Functions import *

class OrdinaryCombination:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer']) 
        self.root.geometry(variables['size'])
        self.root.resizable(0, 0)
        self.data = data

        # Frame
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.label_m = tk.Label(self.frame, text=text["total_poblation"], font=("Arial", 20))
        self.label_n = tk.Label(self.frame, text=text["selected_poblation"], font=("Arial", 20))
        
        # Entries para ingresar los números
        self.entry_m = tk.Entry(self.frame, width=20, font=("Arial", 12))
        self.entry_n = tk.Entry(self.frame, width=20, font=("Arial", 12))
        
        self.solve_button = tk.Button(self.frame, text=text["solve"], font=("Arial", 20), command=self.solve)
        
        self.label_result = tk.Label(self.frame, text="", font=("Arial", 20))
        
        self.label_m.grid(row=0, column=0, padx=10, pady=10)
        self.entry_m.grid(row=1, column=0, padx=10, pady=10)
        self.label_n.grid(row=2, column=0, padx=10, pady=10)
        self.entry_n.grid(row=3, column=0, padx=10, pady=10)
        self.solve_button.grid(row=4, column=0, padx=10, pady=10)
        self.label_result.grid(row=5, column=0, padx=10, pady=10)
    
    def solve(self):
        m_text = self.entry_m.get()
        n_text = self.entry_n.get()
        if m_text.isdigit() and n_text.isdigit():
            m = int(m_text)
            n = int(n_text)
            result = CombinationsWithoutRepetition(total=m, groups=n)
            self.label_result.config(text=str(result))
        else:
            self.label_result.config(text=text["digit_error"])

    def run(self):
        self.root.mainloop()
        
    def stop(self):
        self.root.destroy()
