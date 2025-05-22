import pymysql
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

host = os.getenv("MYSQL_HOST").strip()
port = int(os.getenv("MYSQL_PORT").strip())
user = os.getenv("MYSQL_USER").strip()
password = os.getenv("MYSQL_PASSWORD").strip()
database = os.getenv("MYSQL_DB").strip()

try:
    # Conexão com o banco
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        cursorclass=pymysql.cursors.DictCursor  # para resultados como dicionário
    )
    print("Conexão com o banco realizada com sucesso!")

    with conn.cursor() as cursor:
        sql = "SELECT * FROM orgao WHERE id = %s"
        cursor.execute(sql, (25,))
        resultado = cursor.fetchall()

        if resultado:
            print("Resultado do SELECT:")
            for row in resultado:
                print(row)
        else:
            print("Nenhum registro encontrado para id = 25")

except Exception as e:
    print("Erro durante a conexão ou consulta:", e)

finally:
    if conn:
        conn.close()
