from classes.database import Database
from tkinter import *

db = Database()

import tkinter as tk
import mysql.connector
from tkinter import *



def createAccount():
    query = "SELECT * FROM users WHERE username='"+ Username.get()  +"' AND password='"+ password.get() +"'"
    result = db.query(query)

    if(len(result) > 0):
        my_string_var.set("These credentials are already in use")
        return
    else:
        query = "INSERT INTO users (username, password, first_name, last_name, birth_date, email) VALUES ('" + Username.get() +"','" + password.get() +"','pj', 'holt', '1900-01-01', 'pj@example.com')" 
        result = db.query(query)
        my_string_var.set("Account created")

def login():
    query = "SELECT * FROM users WHERE username='"+ Username.get()  +"' AND password='"+ password.get() +"'"
    result = db.query(query)

    if(len(result) == 0):
        my_string_var.set("Invalid Credentials")
        return

    if(len(result) == 1):
        my_string_var.set("Logged In " + Username.get())
        return


db = Database()
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
my_string_var = StringVar()
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username")
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

test = tk.Label(root, name='error', textvariable=my_string_var)
test.place(x = 50, y = 80)

submitbtn = tk.Button(root, text ="Login",
                      bg ='grey', command = login)
submitbtn.place(x = 50, y = 100, width = 50)

submitbtn = tk.Button(root, text ="Create Account",
                      bg ='grey', command = createAccount)
submitbtn.place(x = 110, y = 100, width = 90)
 
root.mainloop()