import tkinter as tk

from .page import Page


class Dashboard(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)
        self.parent = parent

    def content(self):
        tk.Label(self,  text ="Dashboard").grid(row=0, column=0, padx=10, pady=10)
