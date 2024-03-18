import tkinter as tk
from tkinter import ttk
from res.data import variables, text
from res.Functions import *


class RepitedPermutation:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer'])
        self.root.geometry(variables['size'])
        self.root.resizable(0, 0)
        self.data = data

        # Frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # Labels
        self.label_m = tk.Label(self.frame, text=text["total_poblation"], font=("Helvetica", 14, "bold"))
        self.label_n = tk.Label(self.frame, text=text["repited_poblation"], font=("Helvetica", 14, "bold"))

        # Entries para ingresar los números
        self.entry_m = tk.Entry(self.frame, width=20, font=("Helvetica", 12))
        self.entry_n = tk.Entry(self.frame, width=20, font=("Helvetica", 12))

        # Botón para resolver
        self.solve_button = tk.Button(self.frame, text=text["solve"], font=("Helvetica", 14, "bold"),
                                      command=self.solve)

        # Resultado
        self.label_result = tk.Label(self.frame, text="", font=("Helvetica", 14))

        # Grid layout
        self.label_m.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_m.grid(row=0, column=1, padx=10, pady=10)
        self.label_n.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_n.grid(row=1, column=1, padx=10, pady=10)
        self.solve_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def solve(self):
        m_text = self.entry_m.get()
        n_text = self.entry_n.get()
        if m_text.isdigit() and isTuple(m_text):
            m = int(m_text)
            n = strToTuple(n_text)
            result = PermutationsWithRepetition(total=m, repited_numbers=n)
            self.label_result.config(text=str(result))
        else:
            self.label_result.config(text=text["digit_error"])

    def run(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()
