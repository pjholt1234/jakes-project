import tkinter as tk
from pages.login import Login
from helpers.database import Database
from helpers.user import User
from pages.welcome import Welcome
from pages.dashboard import Dashboard

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        #Global Helper Classes
        self.db = Database()
        self.user = User()
        self.selectedPageId = None

        #Pages
        self.pages = {
            'welcome': {   
                'name': 'Welcome',
                'page': Welcome(self),
            },
            'dashboard':{   
                'name': 'Dashboard',
                'page': Dashboard(self),
            }
        }

        self.generateFrames()
        self.render()

    def generateFrames(self):
        self.buttonframe = tk.Frame(self)
        self.container = tk.Frame(self)
        self.buttonframe.pack(side="top", fill="x", expand=False)
        self.container.pack(side="top", fill="both", expand=True)

    def render(self):
        if(not self.user.loggedIn):
            Login(self).place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
            tk.Button(self.buttonframe, text="Log in", command=Login(self).lift).pack(side="left")
        else:
            self.buttonframe.destroy()
            self.container.destroy()
            
            self.generateFrames()

            for page_id in self.pages:
                self.pages[page_id]['page'].place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

                #Important to use page_id=page_id here!
                tk.Button(self.buttonframe, text=self.pages[page_id]['name'], command=lambda page_id=page_id: self.pageSelection(page_id)).pack(side="left")

            if(self.selectedPageId == None):
                self.pages['welcome']['page'].lift()
            else:
                self.pages[self.selectedPageId]['page'].lift()

    def pageSelection(self, page_id):
        self.selectedPageId = page_id
        print(page_id)
        self.pages[page_id]['page'].lift()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("TEST")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()