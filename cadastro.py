import sqlite3 as conector 
from sqlite3 import DatabaseError
from consulta import consulta
import ipdb
def cadastro(i):

    try:

        conexao = conector.connect("db.av2")
        cursor = conexao.cursor()

        #matricula = int(input("Digite a matricula: "))
        #nome = input("Digite o nome: ")
        #data_nasc = input("Digite a data de nascimento: ")
        #curso = input("Dgite o nome do curso: ")
        #dados = [matricula,nome,data_nasc,curso]

        sql = 'INSERT INTO cadastro (matricula,nome,data_nasc,curso) VALUES (?,?,?,?)'
        #ipdb.set_trace()
        
        cursor.execute(sql,i)
        cursor.fetchall()
        conexao.commit()
        print("Cadastro realizado com sucesso!")
    
    except conector.DatabaseError as err:

        print("{}".format(err))

    finally:
        if (conexao):

            cursor.close()
            conexao.close()
    #cadastro(i)