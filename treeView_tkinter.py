from tkinter import *
from tkinter import ttk

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

# GRADE DE LISTAGEM, TRAZENDO CONTEÚDO DE UMA LISTA OU DE UM BANCO DE DADOS

# LISTA PARA INSERIR NA TREE VIEW
listaNomes = [['0','Victor','11960586785'],['1','B Helder','11920586785'],['2','Biel','11950586785']]

# DECLARANDO A TREE VIEW, COLUNAS E CABEÇALHO
tv = ttk.Treeview(app,columns=('id','nome','fone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)

# DEFININDO CABEÇALHO
tv.heading('id',text="ID")
tv.heading('nome',text="NOME")
tv.heading('fone',text="TELEFONE")

# INSERINDO INFORMAÇÕES COM LAÇO DE REPETIÇÃO
for id,nome,fone in listaNomes:
    tv.insert("","end",values=(id,nome,fone))

tv.pack()

app.mainloop()