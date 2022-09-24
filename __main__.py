import tkinter as tk
from classes.login import Login
from classes.database import Database

print('test', hash('test'))

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.db = Database()

        self.currentPage = Login(self, self.db)
        self.currentPage.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("TEST")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()