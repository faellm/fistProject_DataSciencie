import psycopg2
import csv

# Configurações de conexão
host = 'localhost'
port = 5432
database = 'cienciadedados'
user = 'rafaellaramartins'
password = ''
nome_tabela = 'tabela_parana'

try:
    
    # Conectando ao banco de dados
    conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
    print(f"Conexão realizada com sucesso. Host:{host} | Port:{port} | DataBase: {database}")
    # Criando um cursor
    cur = conn.cursor()
    

    # Verificando se a tabela já existe
    cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (nome_tabela,))
    tabela_existe = cur.fetchone()[0]
    
    if tabela_existe != True:
        
        print("Tabela não achada.")

    if tabela_existe:
        
        # Recuperando os resultados da consulta
        cur.execute(f"SELECT * FROM {nome_tabela}")
        resultados = cur.fetchall()

        # Exibindo os resultados
        for linha in resultados:
            
            display(linha)
            
            
    else:
        print(f"A tabela {nome_tabela} não existe.")
    
finally:
    # Fechando cursor e conexão
    if cur:
        
        cur.close()
        
    if conn:
        
        conn.close()
