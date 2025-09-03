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

# Pede ao usuário o código do produto que deseja remover
try:
    cod_prod = int(input("Digite o código do produto que deseja excluir: "))
except ValueError:
    print("Por favor, digite um número válido para o código do produto.")
    exit()

# Chama a stored procedure que remove o produto do banco
try:
    cursor.execute("EXEC SpExProduto @CodProd = ?", cod_prod)
    conn.commit()  # Confirma a exclusão no banco
    print(f"Produto com código {cod_prod} excluído com sucesso!")
except Exception as e:
    print("Ocorreu um erro ao excluir o produto:", e)
finally:
    # Fecha a conexão e libera recursos
    cursor.close()
    conn.close()
