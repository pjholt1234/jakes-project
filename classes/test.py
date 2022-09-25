import tkinter as tk


class Test(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        tk.Label(self,  text ="TEST").grid(row=0, column=0, padx=10, pady=10)

    def show(self):
        self.lift()