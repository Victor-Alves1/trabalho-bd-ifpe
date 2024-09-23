import pandas as pd
import sqlite3
from functions.create_table import create_table

create_table(
    #nome
    # coluna
    # descrição
    database='mydatabase',
    table_name='Cliente',  
    columns_name=""" 
       ID_cliente INTEGER PRIMARY KEY NOT NULL, --Identificador único do cliente
       Nome VARCHAR(20) NOT NULL, --Nome do Cliente
       Sobrenome VARCHAR(20), --Sobrenome do Cliente
       Genero CHAR(10), --Genero do Cliente
       CPF CHAR(11), --Número do cadastro da pessoa física do cliente 
       Celular CHAR(15) NOT NULL , --Número de telefone 
       E-mail CHAR(20), --endereço do correio eletronico do cliente
       CEP CHAR(8), --Número do endereçamento postal do cliente
       Logradouro CHAR(30), --Nome da rua onde o cliente mora
       Nº_Da_Casa CHAR(10) , --Número da casa onde o cliente mora 
       Complemento CHAR(30), --Informações adicionais que ajudam a esclarecer onde fica localizada a casa do cliente
       Bairro CHAR(20), --Nome do bairro em que o cliente mora
       Cidade CHAR(20), --Nome da cidade em que o cliente mora
       Estado CHAR(15), --Nome do estado em que o cliente mora  
    """,
    values= """
       INSERT INTO Cliente (ID_cliente,Nome,Sobrenome,Genero, CPF, Celular
       E-mail, CEP, Logradouro, N°_Da_Casa, Complemento, Bairro, Cidade, Estado)
       
       VALUES
       (1, '140324202201', 'Thamires', 'Fernandes' , 'Feminino', '100010010-01',
         '81987182384', 'thamires_a_gatinha@hotmail.com', '55607259', 'Rua Tads, 500', 
         'Prox. ao bloco f', 'Universitário', 'Recife', 'Pernambuco' )
"""


)
# create a data example
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# create a connection
conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to save the DataFrame to a table in the database
data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

# closing the connection
conn.close()


########## 
conn = sqlite3.connect('mydatabase.db')

query = """ 
    SELECT Name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""


pd.read_sql_query(query, conn)
