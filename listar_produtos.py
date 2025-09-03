import pyodbc
from prettytable import PrettyTable

# Cria a conexão com o banco remoto
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=mssql-196998-0.cloudclusters.net,10024;'
    'DATABASE=teste;'
    'UID=teste;'
    'PWD=Full@2000;'
    'TrustServerCertificate=yes;'
)

cursor = conn.cursor()

# Pede ao usuário para digitar parte do nome do produto que deseja buscar
nome = input("Digite parte do nome do produto: ")

# Chama a stored procedure passando o nome informado
cursor.execute("EXEC SpSeProduto ?", nome)

# Recupera todos os produtos retornados pela procedure
resultados = cursor.fetchall()

# Organiza os resultados em uma tabela para facilitar a visualização
tabela = PrettyTable()
tabela.field_names = ["CodProd", "DescrProd"]

for row in resultados:
    tabela.add_row([row.CodProd, row.DescrProd])

# Mostra a tabela na tela
print(tabela)
