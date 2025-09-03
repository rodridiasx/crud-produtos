import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=mssql-196998-0.cloudclusters.net,10024;'
        'DATABASE=teste;'
        'UID=teste;'
        'PWD=Full@2000;'
        'TrustServerCertificate=yes;'  # <<< adiciona isso
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print("Conexão bem-sucedida! Resultado do teste:", cursor.fetchone())

except Exception as e:
    print("Deu algum erro na conexão:", e)
