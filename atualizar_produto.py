"""
Arquivo: atualizar_produto.py
Descrição: Script para atualizar a descrição de um produto no banco de dados.
Observações:
- O banco fornecido pelo recrutador não permite criar novas Stored Procedures.
- Este script depende da Stored Procedure 'SpUpdateProduto' já existente.
- Como essa SP não existe no banco de teste, o script não funcionará remotamente.
- O código abaixo demonstra como seria feito o update caso a SP existisse.
"""

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

# Pede ao usuário o código do produto e a nova descrição
cod_prod = int(input("Digite o código do produto que deseja atualizar: "))
descr_prod = input("Digite a nova descrição do produto: ")

# Tenta atualizar o produto usando a SP existente
try:
    cursor.execute("EXEC SpUpdateProduto @CodProd = ?, @DescrProd = ?", cod_prod, descr_prod)
    conn.commit()  # Confirma a alteração no banco
    print("Produto atualizado com sucesso!")
except Exception as e:
    # Caso a SP não exista ou ocorra outro erro
    print("Não foi possível executar o update. Detalhes:", e)
finally:
    # Encerra a conexão e libera recursos
    cursor.close()
    conn.close()
