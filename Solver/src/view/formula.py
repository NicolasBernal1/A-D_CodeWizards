import tkinter as tk
from res.data import variables, text, formula_desc
from res.Functions import *

from view.ordinarycombination import OrdinaryCombination
from view.ordinarypermutation import OrdinaryPermutation
from view.ordinaryvariation import OrdinaryVariation

from view.repitedcombination import RepitedCombination
from view.repitedpermutation import RepitedPermutation
from view.repitedvariation import RepitedVariation


class Formula:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer'])
        self.root.geometry(variables['size'])
        self.root.resizable(0, 0)
        self.data = data

        formula_type = TypeOperation(self.format_data())
        formula_description = formula_desc[formula_type]

        # Frame
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Label for formula identification
        label1_text = text["formula_is"] + " " + formula_type
        label1 = tk.Label(frame, text=label1_text, font=("Helvetica", 14, "bold"))
        label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Label for formula description
        label2 = tk.Label(frame, text=formula_description, font=("Helvetica", 12))
        label2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Button for navigating to different formula views
        button1 = tk.Button(frame, text=text["next"], font=("Helvetica", 14, "bold"))
        button1.grid(row=2, column=0, padx=10, pady=10)

        # Set command for the button based on formula type
        if formula_type == "permutación con repetición":
            button1.config(command=self.goto_repited_permutation)
        elif formula_type == "permutaciones ordinarias":
            button1.config(command=self.goto_ordinary_permutation)
        elif formula_type == "variaciones con repetición":
            button1.config(command=self.goto_repited_variation)
        elif formula_type == "variaciones ordinarias":
            button1.config(command=self.goto_ordinary_variation)
        elif formula_type == "combinación con repetición":
            button1.config(command=self.goto_repited_combination)
        elif formula_type == "combinaciones ordinarias":
            button1.config(command=self.goto_ordinary_combination)
        else:
            print("Error!")

    def format_data(self):
        return tuple(value for value in self.data.values())

    def goto_ordinary_combination(self):
        self.stop()
        ordinary_combination_window = OrdinaryCombination(self.data)
        ordinary_combination_window.run()

    def goto_ordinary_permutation(self):
        self.stop()
        ordinary_permutation_window = OrdinaryPermutation(self.data)
        ordinary_permutation_window.run()

    def goto_ordinary_variation(self):
        self.stop()
        ordinary_variation_window = OrdinaryVariation(self.data)
        ordinary_variation_window.run()

    def goto_repited_combination(self):
        self.stop()
        repited_combination_window = RepitedCombination(self.data)
        repited_combination_window.run()

    def goto_repited_permutation(self):
        self.stop()
        repited_permutation_window = RepitedPermutation(self.data)
        repited_permutation_window.run()

    def goto_repited_variation(self):
        self.stop()
        repited_variation_window = RepitedVariation(self.data)
        repited_variation_window.run()

    def run(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()
