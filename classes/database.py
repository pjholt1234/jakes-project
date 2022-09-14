import mysql.connector
import os
from dotenv import load_dotenv

class Database:
    def __init__(self):
        self._db = self._connection()
        self.connected = self._validateConnection()

    def _connection(self):
        load_dotenv()
        return mysql.connector.connect(
            host=os.getenv('HOST', default=None),
            user=os.getenv('DB_USER', default=None),
            passwd=os.getenv('DB_PASSWORD', default=None),
        )

    def query(self, query):
        mycursor = self._db.cursor()
        mycursor.execute(query)
        return mycursor.fetchall()

    def _validateConnection(self) -> bool:
        return True


db = Database()     

print(db.query("SHOW DATABASES LIKE 'test'"))