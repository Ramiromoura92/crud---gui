# Importando todos os pacotes do tkinter 
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox
from consulta import consulta
from cadastro import cadastro
from update import update
from delete import delete
import ipdb

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando janela ###############
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=True, height=True)#Bloqueando largura e altura

################# Dividindo janela ###############

frame_cima = Frame(janela,width=310, height=50, background=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela,width=310, height=403, background=co1, relief='flat')
frame_baixo.grid(row=1, column=0,sticky=NSEW,padx=0,pady=1)

frame_direita = Frame(janela,width=588, height=403, background=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2,padx=1,pady=0,sticky=NSEW)

################# Label cima ###############

app_nome = Label(frame_cima,text='Formulario de cadastro',anchor=NW, font=('Ivy 10 bold'),bg = co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

#variavel global 
global tabela
#funcao inserir
def inserir():
    matricula = entry_matricula.get()
    nome = entry_name.get()
    data_nasc = entry_data_nasc.get()
    curso = entry_curso.get()

    lista = [matricula,nome,data_nasc,curso]

    if nome == '':
        messagebox.showerror('Erro','O nome nao pode ser vazio')
    else:
        cadastro(lista)
        #ipdb.set_trace()
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        #limpando após insercao de dados
        entry_matricula.delete(0,'end')
        entry_name.delete(0,'end')
        entry_data_nasc.delete(0,'end')
        entry_curso.delete(0,'end')
    
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar_banco()

def atualizar():

    try:
    
    
        tabela_dados = tabela.focus()
        tabela_dicionario = tabela.item(tabela_dados)
        tabela_lista = tabela_dicionario['values']

        valor = tabela_lista[0] #pegando apenas o primeiro valor como referencia 
        
        
        entry_matricula.delete(0,'end')
        entry_name.delete(0,'end')
        entry_data_nasc.delete(0,'end')
        entry_curso.delete(0,'end')

        entry_matricula.insert(0, tabela_lista[0])
        entry_name.insert(0, tabela_lista[1])
        entry_data_nasc.insert(0, tabela_lista[2])
        entry_curso.insert(0, tabela_lista[3])

        def atualizar_info():
            matricula = entry_matricula.get()
            nome = entry_name.get()
            data_nasc = entry_data_nasc.get()
            curso = entry_curso.get()

            lista = [matricula,nome,data_nasc,curso]

            if nome == '':
                messagebox.showerror('Erro','O nome nao pode ser vazio')
            else:
                update(lista)
                #ipdb.set_trace()
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                #limpando após insercao de dados
                entry_matricula.delete(0,'end')
                entry_name.delete(0,'end')
                entry_data_nasc.delete(0,'end')
                entry_curso.delete(0,'end')
            
            for widget in frame_direita.winfo_children():
                widget.destroy()
            
            mostrar_banco()

        b_confirmar = Button(frame_baixo,command=atualizar_info, text='Confirmar',anchor=NW, font=('Ivy 7 bold'),bg = co2, fg=co1, relief='raised',overrelief='ridge')
        b_confirmar.place(x=110,y=370)


            
    except IndexError as err:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela!')


def deletar_info():

    tabela_dados = tabela.focus()
    tabela_dicionario = tabela.item(tabela_dados)
    tabela_lista = tabela_dicionario['values']

    matricula = tabela_lista[0]

    delete(matricula)
    mostrar_banco()

    

################# Configurando o frame de baixo ###############

################# Configurando as entradas ###############
#Matricula
label_matricula = Label(frame_baixo,text='Matricula *',anchor=NW, font=('Ivy 10 bold'),bg = co1, fg=co4, relief='flat')
label_matricula.place(x=10, y=10)
entry_matricula = Entry(frame_baixo, width=45, justify='left',relief='solid')
entry_matricula.place(x=15, y=40)

#nome
label_name = Label(frame_baixo,text='Nome *',anchor=NW, font=('Ivy 10 bold'),bg = co1, fg=co4, relief='flat')
label_name.place(x=10, y=70)
entry_name = Entry(frame_baixo, width=45, justify='left',relief='solid')
entry_name.place(x=15, y=100)

#Data_nasc
label_data_nasc = Label(frame_baixo,text='Data_nasc *',anchor=NW, font=('Ivy 10 bold'),bg = co1, fg=co4, relief='flat')
label_data_nasc.place(x=10, y=130)
entry_data_nasc = DateEntry(frame_baixo, width=12,bg='darkblue',fg='white',borderwidth=2,year=2022)
entry_data_nasc.place(x=15, y=160)

#Curso
label_curso = Label(frame_baixo,text='Curso *',anchor=NW, font=('Ivy 10 bold'),bg = co1, fg=co4, relief='flat')
label_curso.place(x=10, y=190)
entry_curso = Entry(frame_baixo, width=20, justify='left',relief='solid')
entry_curso.place(x=15, y=220)


#botão inserir

b_inserir = Button(frame_baixo,command=inserir, text='Inserir',anchor=NW, font=('Ivy 9 bold'),bg = co6, fg=co1, relief='raised',overrelief='ridge')
b_inserir.place(x=15,y=340)

#botão atualizar

b_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar',anchor=NW, font=('Ivy 9 bold'),bg = co2, fg=co1, relief='raised',overrelief='ridge')
b_atualizar.place(x=110,y=340)

#botão deletar

b_deletar = Button(frame_baixo,command=deletar_info, text='Deletar',anchor=NW, font=('Ivy 9 bold'),bg = co7, fg=co1, relief='raised',overrelief='ridge')
b_deletar.place(x=205,y=340)

################# frame direita ###############



def mostrar_banco():

    global tabela

    lista = consulta()

    #Criando cabeario
    tabela_cabecario = ['matricula','nome','data-nasc','curso']

    #criando a tabela dentro do frame
    tabela = ttk.Treeview(frame_direita,selectmode='extended', columns=tabela_cabecario,show='headings')


    #scrolar para vertical 

    scrol_vert = ttk.Scrollbar(frame_direita, orient='vertical',command=tabela.yview)

    #scrolar para horizontal 

    scrol_hori = ttk.Scrollbar(frame_direita, orient='horizontal',command=tabela.xview)

    tabela.configure(yscrollcommand=scrol_vert.set, xscrollcommand=scrol_hori.set)

    tabela.grid(column=0,row=0,sticky='nsew')
    scrol_vert.grid(column=1,row=0,sticky='ns')
    scrol_hori.grid(column=0,row=1,sticky='ew')
    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center"]
    h=[170,140,100,350]
    n=0

    for col in tabela_cabecario:
        tabela.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tabela.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in lista:
        tabela.insert('', 'end', values=item)

mostrar_banco()


janela.mainloop()



