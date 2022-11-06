import tkinter as tk
from abc import ABC, abstractmethod


class Page(tk.Frame, ABC):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.content()
        
    def show(self):
        self.lift()

    @abstractmethod
    def content(self):
        pass

