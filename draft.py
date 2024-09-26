import pandas as pd
import sqlite3
from functions.create_table import create_table

create_table(
    database='mydatabase',
    table_name='cadastro_cliente',
    columns_desc="""
        ID_CLIENTE	INTEGER PRIMARY KEY NOT NULL,
        CPF	varchar(11)	NOT NULL,
        NOME varchar(100)	NOT NULL,
        DATA_DE_NASCIMENTO	varchar(20)	NOT NULL,
        NACIONALIDADE varchar(20) NOT NULL,
        ID_ENDEREÇO	varchar(20)	NOT NULL
    """
)

data_cliente = pd.DataFrame({
    'ID_CLIENTE': [1, 2, 3, 4],
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

create_table(
    database='mydatabase',
    table_name='reservas',
    columns_desc="""
        ID_RESERVA	INTEGER PRIMARY KEY NOT NULL,
        ID_CLIENTE	INTEGER NOT NULL,
        ID_QUARTO	INTEGER NOT NULL,
        CHECKIN	varchar(20) NOT NULL,
        CHECKOUT	varchar(20) NOT NULL
    """
)

data_reserva = pd.DataFrame({
    'ID_RESERVA': [1, 2, 3, 4],
    'ID_CLIENTE': [4, 3, 2, 1],
    'ID_QUARTO': [3, 2, 1, 4],
    'CHECKIN': ['01-02-2024', '10-02-2024', '02-02-2024', '30-02-2024'],
    'CHECKOUT': ['09-02-2024', '19-02-2024', '09-02-2024', '01-02-2024']
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

data_reserva.to_sql(
    'reservas', conn,
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
query_reservas = """ 
    SELECT * 
    FROM reservas
"""

select_clientes = pd.read_sql_query(query_clientes, conn)
print(select_clientes)
print('------------------------------------------------------------------')
select_quartos = pd.read_sql_query(query_quartos, conn)
print(select_quartos)
print('------------------------------------------------------------------')
select_reservas = pd.read_sql_query(query_reservas, conn)
print(select_reservas)

conn.close()