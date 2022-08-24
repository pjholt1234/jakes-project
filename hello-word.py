 # import everything from tkinter module
from tkinter import *

class App:
    def __init__(self):
        self.tk = Tk()
        self.count = 0
        self.countLabel = StringVar()
        self.setText()
        self.setUp()
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

    def setText(self):
        self.countLabel.set(self.count)

    def counter(self):
        print(self.count)
        self.count = self.count+1
        self.setText()

    def buildUi(self):
        button = Button(self.tk, text=' 1 ', fg='black', bg='red', command=self.counter, height=1, width=7)
        button.grid(row=2, column=2)

        label = Label ( self.tk, textvariable=self.countLabel, text=' 1 ')
        label.grid(row=3, column=3)

p1 = App()


