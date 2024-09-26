import sqlite3

def create_db(  
    database_name:str      
) -> sqlite3.Connection:

    return sqlite3.connect(f'{database_name}.db')