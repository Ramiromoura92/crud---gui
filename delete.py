import sqlite3 as conector
from sqlite3 import DatabaseError

def delete(matricula):
    try:
        conexao = conector.connect("db.av2")
        cursor = conexao.cursor()

        #matricula = int(input("Digite a matricula: "))
            
        #sql = f'UPDATE cadastro SET nome = {nome},data_nasc = {data_nasc},curso = {curso} where matricula = {matricula}'
        sql = f'DELETE FROM cadastro where matricula = {matricula}'

        cursor.execute(sql)
        cursor.fetchall()
        conexao.commit()
    except conector.DatabaseError as err:
        
        print(err)
    
    finally:
        if (conexao):
            cursor.close()
            conexao.close()



    
