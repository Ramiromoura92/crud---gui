import sqlite3 as conector
from sqlite3 import DatabaseError

def update(i):
    try:
        
        conexao = conector.connect("db.av2",timeout=10)
        cursor = conexao.cursor()
        """
        matricula = int(input("Digite a matricula: "))
        nome = input("Digite o nome: ")
        data_nasc = input("Digite a data de nascimento: ")
        curso = input("Dgite o nome do curso: ")
        """
        #dados = [nome,data_nasc,curso,matricula]

        sql = f"""UPDATE cadastro SET nome = '{i[1]}',data_nasc = {i[2]},curso = '{i[3]}' where matricula = {i[0]}"""
        #sql = 'UPDATE cadastro SET nome = ?,data_nasc = ?,curso = ? where matricula = ? '
    

        cursor.execute(sql)
        #import ipdb; ipdb.set_trace()
        cursor.fetchall()
        conexao.commit()
    except conector.DatabaseError as err:
        
        print(err)
    
    finally:
        if (conexao):
            cursor.close()
            conexao.close()



    
