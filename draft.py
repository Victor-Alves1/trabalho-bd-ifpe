import pandas as pd
import sqlite3
from functions.create_table import create_table

create_table(
    database='mydatabase',
    table_name='cadastro_cliente',
    columns_desc="""
        ID CLIENTE	INTEGER PRIMARY KEY NOT NULL,
        CPF	varchar(11)	NOT NULL,
        NOME varchar(100)	NOT NULL,
        DATA_DE_NASCIMENTO	varchar(20)	NOT NULL,
        NACIONALIDADE varchar(20) NOT NULL,
        ID_ENDEREÇO	varchar(20)	NOT NULL
    """
)

data_cliente = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'CPF': ['111', '222', '333', '4444'],
    'NOME': ['Victor', 'Tamires', 'Liliane', 'Guilherme'],
    'DATA_DE_NASCIMENTO': ['01-02-2000', '02-04-1998', '04-06-1996', '06-08-2002'],
    'NACIONALIDADE': ['Brasileiro', 'Brasileiro', 'Brasileiro', 'Brasileiro'],
    'ID_ENDEREÇO': ['ab', 'cd', 'de', 'fg']
})

create_table(
    database='mydatabase',
    table_name='cadastro_quartos',
    columns_desc="""
        ID_Quarto	INTEGER PRIMARY KEY NOT NULL,
        Numero	varchar(2) NOT NULL,
        Posicao	varchar(10) NOT NULL,
        Andar	varchar(1) NOT NULL,
        Acessibilidade	varchar(3) NOT NULL,
        camas	INTEGER NOT NULL,
        pessoas	INTEGER NOT NULL,
        Valor	real NOT NULL
    """
)

data_quarto = pd.DataFrame({
    'ID_Quarto': [1, 2, 3, 4],
    'Numero': ['55', '10', '42', '33'],
    'Posicao': ['Frente', 'Fundo', 'Leste', 'Oeste'],
    'Andar': ['1', '2', '2', '8'],
    'Acessibilidade': ['sim', 'não', 'sim', 'não'],
    'camas': [1, 2, 1, 5],
    'pessoas': [2, 3, 1, 5],
    'Valor': [1.1,2.2,3.3,4.5]
})

conn = sqlite3.connect('mydatabase.db')

data_cliente.to_sql(
    'cadastro_cliente', conn,
    if_exists='replace',
    index=False
)

data_quarto.to_sql(
    'cadastro_quartos', conn,
    if_exists='replace',
    index=False
)

conn.close()

conn = sqlite3.connect('mydatabase.db')

query_clientes = """ 
    SELECT * 
    FROM cadastro_cliente
"""
query_quartos = """ 
    SELECT * 
    FROM cadastro_quartos
"""

select_clientes = pd.read_sql_query(query_clientes, conn)
print(select_clientes)
print('------------------------------------------------------------------')
select_quartos = pd.read_sql_query(query_quartos, conn)
print(select_quartos)

conn.close()