import tkinter as tk
from tkinter import ttk
from res.data import variables, text, developers
from res.Functions import *
from view.welcome import Welcome

class MainPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(variables["name"] + " " + variables["developer"])
        self.root.geometry(variables['size'])
        self.root.resizable(0, 0)
        self.data = {}

        # Frame
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        img_label = tk.Label(frame, text="Placeholder for image")
        img_label.grid(row=0, column=0, padx=10, pady=10)

        # Labels for developers' names
        names = developers
        for idx, name in enumerate(names, start=1):
            label = tk.Label(frame, text=name, font=("Helvetica", 12))
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

        # Button for navigating to the next frame
        next_button = ttk.Button(frame, text=text["next"], command=self.next_frame)
        next_button.grid(row=len(names) + 1, column=0, padx=10, pady=10)

    def next_frame(self):
        self.stop()
        frame = Welcome()
        frame.run()

    def run(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()
