import sqlite3
from pathlib import Path
from DataBaseManager import sqlite
from utils import commit_errors

DB = "./database/database.db"

try:
    MyObj= sqlite(DB)
    MyObj.CreateDb()
except Exception as err:
    commit_errors(err)
    raise err
