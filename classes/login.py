import tkinter as tk
import bcrypt

class Login(tk.Frame):
    def __init__(self, parent, db):
        tk.Frame.__init__(self, parent)

        self.db = db
        self.user = None
        self.my_string_var = tk.StringVar()

        tk.Label(self,  text ="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username = tk.Entry(self, width = 35)
        self.username.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text ="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password = tk.Entry(self, show="*", width = 35)
        self.password.grid(row=1, column=1, padx=10, pady=10)

        self.error = tk.Label(self, name='error')
        self.error.grid(row=2, column=0, padx=10, pady=10)

        tk.Button(self, text ="Login", bg ='grey', command = self.login).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text ="Create Account", bg ='grey', command = self.createAccount).grid(row=3, column=1, padx=10, pady=10)

    def createAccount(self):
        password = bcrypt.hashpw(self.password.get().encode('utf8'), bcrypt.gensalt()).decode('utf-8')
        query = "SELECT * FROM users WHERE username='"+ self.username.get()  +"'"
        result = self.db.query(query)

        if(len(result) > 0):
            self.error.config(text="These credentials are already in use")
        else:
            query = "INSERT INTO users (username, password, first_name, last_name, birth_date, email) VALUES ('" + self.username.get() +"','" + password +"','pj', 'holt', '1900-01-01', 'pj@example.com')" 
            result = self.db.query(query)
            self.error.config(text="Account created")

    def login(self):
        query = "SELECT * FROM users WHERE username='"+ self.username.get()  +"' LIMIT 1"
        result = self.db.query(query)

        if(len(result) == 0):
            self.error.config(text="No user "+ self.username.get() +" found")
            return None

        if(len(result) == 1):
            if(bcrypt.checkpw(self.password.get().encode('utf8'), result[0][6].encode('utf8'))):
                query = "SELECT * FROM users WHERE username='"+ self.username.get()  +"' LIMIT 1"
                result = self.db.query(query)
                self.error.config(text="Logged In " + self.username.get())
                self.user = result[0]
            