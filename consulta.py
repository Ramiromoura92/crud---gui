import sqlite3 as conector
from sqlite3 import DatabaseError

def consulta():
    lista = []
    try:
        conexao = conector.connect("db.av2")
        cursor = conexao.cursor()

        #matricula = int(input("Digite a matricula: "))

        #sql = f'SELECT * FROM cadastro where matricula = {matricula}'
        sql = 'SELECT * FROM cadastro'
        cursor.execute(sql)
        informacao = cursor.fetchall()

        for i in informacao:
            lista.append(i)
        return lista
        #conexao.commit()
    
    except conector.DatabaseError as err:
        print(err)
    
    finally:
        if (conexao):
            cursor.close()
            conexao.close()

#consulta()
