import tkinter as tk
from tkinter import ttk
from res.data import variables, text
from src.view.formula import Formula

class Welcome:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(variables['name'] + " - " + variables['developer']) 
        self.root.geometry(variables['size'])
        self.root.resizable(0,0)
        self.data = {}

        # Frame
        frame = tk.Frame(self.root)
        frame.pack()

        # ------------------------------#
        # 1st question
        quest1 = tk.Label(frame, text=text["quest1"])
        quest1.grid(row=0, column=0, padx=10, pady=10, sticky="w") 

        # Control variable for the first question
        self.selection1 = tk.StringVar(value=text["true"])

        # Buttons for yes - no
        yes_button1 = ttk.Radiobutton(frame, 
                                      text=text["true"], 
                                      value=text["true"], 
                                      variable=self.selection1)
        
        yes_button1.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        no_button1 = ttk.Radiobutton(frame, 
                                     text=text["false"], 
                                     value=text["false"], 
                                     variable=self.selection1)
        
        no_button1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        # ------------------------------#
        # 2nd question
        quest2 = tk.Label(frame, text=text["quest2"])
        quest2.grid(row=3, column=0, padx=10, pady=10, sticky="w") 

        # Control variable for the secound question
        self.selection2 = tk.StringVar(value=text["true"])

        # Buttons for yes - no
        yes_button2 = ttk.Radiobutton(frame, 
                                      text=text["true"], 
                                      value=text["true"], 
                                      variable=self.selection2)
        
        yes_button2.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        no_button2 = ttk.Radiobutton(frame, 
                                     text=text["false"], 
                                     value=text["false"], 
                                     variable=self.selection2)
        
        no_button2.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        # ------------------------------#
        # 3th question
        quest3 = tk.Label(frame, text=text["quest3"])
        quest3.grid(row=6, column=0, padx=10, pady=10, sticky="w") 

        # Control variable for the third question
        self.selection3 = tk.StringVar(value=text["true"])

        # Buttons for yes - no
        yes_button3 = ttk.Radiobutton(frame, 
                                      text=text["true"], 
                                      value=text["true"], 
                                      variable=self.selection3)
        
        yes_button3.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        no_button3 = ttk.Radiobutton(frame, 
                                     text=text["false"], 
                                     value=text["false"], 
                                     variable=self.selection3)
        
        no_button3.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        
        #--------------------------------
        # Button to send data
        send_data = ttk.Button(frame, text=text["next"], command=self.next_frame)
        send_data.grid(row=9, column=0, padx=10, pady=10)

    def get_data(self):
        
        if self.selection1.get() == text["true"]:
            self.data["ans1"] = True
        else:
            self.data["ans1"] = False

        if self.selection2.get() == text["true"]:
            self.data["ans2"] = True
        else:
            self.data["ans2"] = False

        if self.selection3.get() == text["true"]:
            self.data["ans3"] = True
        else:
            self.data["ans3"] = False

        return self.data

    def next_frame(self):
        self.stop()
        
        self.get_data()
        next_frame = Formula(self.data)
        next_frame.run()
        

    def run(self):
        self.root.mainloop()
        
    def stop(self):
        self.root.destroy()
