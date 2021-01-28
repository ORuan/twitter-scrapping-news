import sqlite3
from pathlib import Path
DB = "./database/database.db"



class TableManager():
    def __init__(self, path_db, **kwargs):
        self.db = path_db
        self.db_name = kwargs.get('db_name')

    def create_or_alter(self):
        try:
            sqliteConnection = sqlite3.connect(self.db)
            cursor = sqliteConnection.cursor()
            cursor.execute(f'CREATE TABLE {self.db_name} id INTEGER PRIMARY KEY')
            print("Database created and Successfully Connected to SQLite")
        except sqlite3.Error as error:
            print("Error while connecting to sqlite :", error)
            sqliteConnection.close()
        finally:
            if (sqliteConnection):
                sqliteConnection.commit()
                sqliteConnection.close()
                print("The SQLite connection is closed")
            else:
                print("Have problems in path of db")