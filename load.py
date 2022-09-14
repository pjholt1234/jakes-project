from classes.database import Database

db = Database()     

print(db.query("SHOW DATABASES LIKE 'test'"))