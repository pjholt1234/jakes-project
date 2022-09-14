import mysql.connector as mysql
import os
from dotenv import load_dotenv
from os.path import exists

class Database:
    def __init__(self)  -> None:
        self._db_host   = None
        self._db_user   = None
        self._db_password = None
        self._db_name   = None
        self._connected  = False


        self._configCheck()
        self._db = self._connection()

    def _configCheck(self):
        load_dotenv()
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../.env')

        if(exists(filename) == False):
            print('Missing ".env" File')
            return False

        if(os.getenv('HOST', default=None) == None):
            print('Missing "HOST" env value')
            return False

        if(os.getenv('DB_USER', default=None) == None):
            print('Missing "DB_USER" env value')
            return False

        if(os.getenv('DB_PASSWORD', default=None) == None):
            print('Missing "DB_PASSWORD" env value')
            return False

        if(os.getenv('DB_NAME', default=None) == None):
            print('Missing "DB_NAME" env value')
            return False    

        self._db_host       = os.getenv('HOST', default=None)
        self._db_user       = os.getenv('DB_USER', default=None)
        self._db_password   = os.getenv('DB_PASSWORD', default=None)
        self._db_name       = os.getenv('DB_NAME', default=None)

        return True

    def _connection(self):
        try:
            connection = mysql.connect(
                host=self._db_host,
                user=self._db_user,
                password=self._db_password,
                database=self._db_name
            )
        
        except (mysql.Error, mysql.Warning) as e:
            self._connected = False
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                print('MySQL Connected')
                self._connected = True
                return connection
    

    def query(self, query):
        if(self._connected):
            try:
                mycursor = self._db.cursor()
                mycursor.execute(query)
            except (mysql.Error, mysql.Warning) as e:
                print("Error while running query: '" + query + "': ", e)
                return None
            finally:
                print('Fetching..')
                return mycursor.fetchall()     
        else:
            print("No Database Connection")
            return None
