from tkinter import *
from tkinter import ttk

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

lb_canal=Label(app,text="CFB Cursos")
lb_nome=Label(app,text="Digite seu nome: ")
lb_idade=Label(app,text="Informe sua idade: ")

et_nome=Entry(app)
et_idade=Entry(app)

btn=Button(app,text="Youtube")

# 'COLUMNSPAN' UNE COLUMNS, CENTRALIZANDO O QUE VOCÊ QUISER ENTRE AS X COLUNAS
# 'ROWSPAN' UNE ROWS, CENTRALIZANDO O QUE VOCÊ QUISER ENTRE AS X LINHAS
lb_canal.grid(column=0,row=0,columnspan=2,pady=15) # COM GRID TUDO É POSICIONADO EM UMA TABELA COM COLUNAS E LINHAS
lb_nome.grid(column=0,row=1,sticky='w')
et_nome.grid(column=0,row=2,sticky='w')
lb_idade.grid(column=1,row=1,sticky='w',padx=5)
et_idade.grid(column=1,row=2,sticky='w',padx=5)
# 'PADX' OU 'PADY' DÁ ESPAÇAMENTO NO PLANO X OU NO Y
# VALORES PARA STICKY, NORTE('n'), SUL9('s'), LESTE('e'), OESTE('w')
# 'STICKY' MUDAR A POSIÇÃO DO TESTO

app.mainloop()