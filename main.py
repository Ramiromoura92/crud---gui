import sqlite3 as conector
from sqlite3 import DatabaseError

def criar_banco():

    try:
        print("Criando banco de dados...")

        conexao = conector.connect("db.av2")
        cursor = conexao.cursor()
        
        sql = 'CREATE TABLE cadastro ( matricula int NOT NULL, nome TEXT, data_nasc DATE, curso TEXT, PRIMARY KEY(matricula))'
        cursor.execute(sql)
        cursor.fetchall()
        cursor.commit()
    except conector.DatabaseError as err:

        print("Erro de {}".format(err))
    
    finally:
        if (conexao):
            cursor.close()
            conexao.close()
            
        print("Banco de dados criado com sucesso!")
criar_banco()