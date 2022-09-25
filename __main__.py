import tkinter as tk
from classes.login import Login
from classes.database import Database
from classes.user import User
from classes.test import Test

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        #Global Helper Classes
        self.db = Database()
        self.user = User()
        self.currentPage = None

        #Pages
        self.pages = [
            {   
                'name': 'login',
                'page': Login(self)
            },
            {   
                'name': 'test',
                'page': Test(self)
            }
        ]

                
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        for page in self.pages:
            page['page'].place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            tk.Button(buttonframe, text="Page 1", command=page['page'].lift).pack(side="left")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("TEST")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()