import sqlite3

def create_table(
    database:str,
    table_name:str,
    columns_desc:str
) -> None:

    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(
   f"""
    CREATE TABLE IF NOT EXISTS {table_name}
       ({columns_desc}) 
    """
)

    conn.close()