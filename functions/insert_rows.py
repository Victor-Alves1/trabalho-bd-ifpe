import sqlite3

def insert_one_row(
        database_name: str,
        table_name: str,
        columns_name: str,
        values: str
) -> None:
    
    database_name2 = f'{database_name}.db'
    
    conn = sqlite3.connect(database_name2)
    cursor = conn.cursor()

    query = f"""
    INSERT INTO {table_name} ({columns_name})
    VALUES ({values})
    """
    cursor.execute(query)
    conn.commit()
    conn.close()
    return None