import pyodbc

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

# Pede ao usuário para informar os dados do produto que deseja criar
cod_prod = input("Digite o código do produto: ")
descr_prod = input("Digite a descrição do produto: ")

# Chama a stored procedure que adiciona o produto ao banco
cursor.execute("EXEC SpGrProduto ?, ?", cod_prod, descr_prod)
conn.commit()  # Confirma a inserção no banco

# Mensagem de confirmação
print(f"Produto '{descr_prod}' criado com sucesso!")
