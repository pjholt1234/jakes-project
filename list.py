 # import everything from tkinter module
from tkinter import *

class App:
    def __init__(self):
        self.tk = Tk()
        self.setUp()
        self.itemsCount = 0
        self.items = []
        self.buildUi()
        self.tk.mainloop()

    def setUp(self):
        #Title    
        self.tk.title("Test")

        #Fullscreen toggle with f11
        self.tk.bind("<F11>", lambda event: self.tk.attributes("-fullscreen",
                                        not self.tk.attributes("-fullscreen")))

        #Bind Esacpe to close program
        self.tk.bind('<Escape>', lambda e: self.tk.destroy())

        self.navBar = Frame(self.tk).grid(row=1, column=1)
        self.body   = Frame(self.tk).grid(row=2, column=1)           

    def getText(self):
        value = self.tk.nametowidget(".inputBox").get("1.0",'end-1c')
        self.items.append(self.itemsCount)
        frameName = 'item-' + str(self.itemsCount)

        item = Frame(self.tk, name=frameName).grid(row=1, column=1)

        labelName = "label-" + str(self.itemsCount)
        Label (item, name=labelName, height=1, width = 20, bd=2, text=value).grid(row=2+len(self.items), column=1)
        buttonName = "del-" + str(self.itemsCount)
        Button(item, name=buttonName, command= lambda name = buttonName: self.getButton(name), text=' Del ', fg='white', bg='red', height=1, width=7).grid(row=2+len(self.items), column=2)

        self.itemsCount = self.itemsCount + 1

    def getButton(self, name):
        id = name.split('-')[1]
        self.tk.nametowidget(".label-"+id).destroy()
        self.tk.nametowidget(".del-"+id).destroy()
        
        print('Deleted item-'+id)

    def buildUi(self):
        
        inputBox = Text(self.navBar, bd=4, height=1, width = 20, name="inputBox").grid(row=1, column=1)
        button = Button(self.navBar, text=' Add ', fg='white', bg='red', command = self.getText, height=1, width=7).grid(row=1, column=2)

App()


