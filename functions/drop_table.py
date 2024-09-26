import sqlite3

def drop_table(
    database:str,
    table_name:str
) -> None:
        
    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"""
        DROP TABLE {table_name}         
    """)

    conn.close()