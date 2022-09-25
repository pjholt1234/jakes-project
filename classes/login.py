import tkinter as tk
import bcrypt

class Login(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        tk.Label(self,  text ="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username = tk.Entry(self, width = 35)
        self.username.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text ="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password = tk.Entry(self, show="*", width = 35)
        self.password.grid(row=1, column=1, padx=10, pady=10)

        self.status = tk.Label(self, name='status')
        self.status.grid(row=2, column=0, padx=10, pady=10)

        tk.Button(self, text ="Login", bg ='grey', command = self.login).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text ="Create Account", bg ='grey', command = self.createAccount).grid(row=3, column=1, padx=10, pady=10)    
        
    def show(self):
        self.lift()

    def createAccount(self):
        # Create account method, handles storage of new account details
        password = bcrypt.hashpw(self.password.get().encode('utf8'), bcrypt.gensalt()).decode('utf-8')
        query = "SELECT * FROM users WHERE username='"+ self.username.get()  +"'"
        result = self.parent.db.query(query)

        if(len(result) > 0):
            self.setStatus(text="These credentials are already in use", text_colour = '#FF0000')
        else:
            query = "INSERT INTO users (username, password, first_name, last_name, birth_date, email) VALUES ('" + self.username.get() +"','" + password +"','pj', 'holt', '1900-01-01', 'pj@example.com')" 
            result = self.parent.db.query(query)
            self.setStatus(text="Account Created For: " + self.username.get(), text_colour = '#00FF00')

    def login(self):
        #Authenticates User and hydrates user model
        query = "SELECT * FROM users WHERE username='"+ self.username.get()  +"' LIMIT 1"
        result = self.parent.db.query(query)

        if(len(result) == 0):
            self.setStatus(text="No user " + self.username.get() +" found", text_colour = '#FF0000')

        elif(len(result) == 1):
            if(bcrypt.checkpw(self.password.get().encode('utf8'), result[0][6].encode('utf8'))):
                query = "SELECT * FROM users WHERE username='"+ self.username.get()  +"' LIMIT 1"
                result = self.parent.db.query(query)

                self.setStatus(text="Logged In " + self.username.get(), text_colour = '#00FF00')

                self.parent.user.hydrate(result[0][0],result[0][1], result[0][2])
            
            else: 
                self.setStatus(text="Invalid Password", text_colour = '#FF0000')

    def setStatus(self, text = '', text_colour = '#000000', bg_colour = '#BEBEBE'):
        self.status.config(text=text, fg = text_colour, background = bg_colour)