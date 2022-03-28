import tkinter as TK
import sqlite3

def create():
    Database = sqlite3.connect(NomeDBIN.get()+'.db')
    DBcursor = Database.cursor()                        #criação do .db e do cursor são comandos python
    DBcursor.execute("CREATE TABLE TESTE(texto text)")  #atividades dentro da tabela tem comando SQL dentro de ()
    Database.commit()  #salva alterações
    Database.close()    #fecha conexão

def gravador():
    Database = sqlite3.connect(NomeDBIN.get()+'.db')
    DBcursor = Database.cursor()
    nomefile = NomeDBIN.get()+'.db'
    DBcursor.execute("INSERT INTO  TESTE VALUES(:texto)",{'texto': TextIn.get()})
    TextIn.delete(0, TK.END)
    Database.commit()
    Database.close()

def consulta():
    Database = sqlite3.connect(NomeDBIN.get()+'.db')
    DBcursor=Database.cursor()
    DBcursor.execute("SELECT *, oid FROM TESTE")
    infos = DBcursor.fetchall() #depois de selecionar as linhas no banco de dados fetch traz as infor para o python
    print(infos)
    Database.commit()
    Database.close()
    
raiz=TK.Tk()
raiz.geometry("300x400")
NomeDBIN=TK.Entry(raiz,width=50)
NomeDBIN.grid(row=0,column=0)
ConectarB = TK.Button(raiz,text='Criar/Conectar ao banco de Dados',command=create)
ConectarB.grid(row=1,column=0)
TextIn=TK.Entry(raiz,width=50)
TextIn.grid(row=2,column=0)
GravarBanco = TK.Button(raiz,text='Gravar',command=gravador)
GravarBanco.grid(row=3,column=0)
ConsultaBanco = TK.Button(raiz,text="o que tem lá?",command=consulta)
ConsultaBanco.grid(row=4,column=0)
raiz.mainloop()