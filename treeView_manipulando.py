from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# FUNÇÕES DE MANIPULAÇÃO DE DADOS
def inserir():
    if vid.get()=="" or vnome.get()=="" or vfone.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    tv.insert("", "end", values=(vid.get(),vnome.get(),vfone.get()))
    vid.delete(0,END)
    vnome.delete(0,END)
    vfone.delete(0,END)
    vid.focus()

def deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um objeto a ser deletado")

def obter():
    try:
        itemSelecionado = tv.selection()[0]
        #valores=tv.item(itemSelecionado,"values") TRAZ TODOS OS VALORES
        #print(valores)
        valores=tv.item(itemSelecionado,"values")
        print("ID........: " + valores[0])
        print("Nome......: " + valores[1]) # TRAZ APENAS O QUE EU QUISER, ESPECIFICANDO COM []
        print("Telefone..: " + valores[2])
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um objeto a ser mostrado")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

# GRADE DE LISTAGEM, TRAZENDO CONTEÚDO DE UMA LISTA OU DE UM BANCO DE DADOS

# PEDIR INFORMAÇÕES AO USUÁRIO
lbID=Label(app,text="ID")#,anchor=W
vid=Entry(app)

lbNOME=Label(app,text="NOME")#,anchor=W
vnome=Entry(app)

lbFONE=Label(app,text="FONE")#,anchor=W
vfone=Entry(app)

# DECLARANDO A TREE VIEW, COLUNAS E CABEÇALHO
tv = ttk.Treeview(app,columns=('id','nome','fone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)

# DEFININDO CABEÇALHO
tv.heading('id',text="ID")
tv.heading('nome',text="NOME")
tv.heading('fone',text="TELEFONE")

# BOTÕES DE MANIPULAÇÃO DE DADOS
btn_inserir=Button(app,text="Inserir dados",command=inserir)
btn_deletr=Button(app,text="Deletar dados",command=deletar)
btn_obter=Button(app,text="Obter dados",command=obter)

# GRID COM OS OBJETOS
lbID.grid(column=0,row=0,sticky='w')
vid.grid(column=0,row=1)

lbNOME.grid(column=1,row=0,sticky='w')
vnome.grid(column=1,row=1)

lbFONE.grid(column=2,row=0,sticky='w')
vfone.grid(column=2,row=1)

tv.grid(column=0,row=3,columnspan=3,pady=3)

btn_inserir.grid(column=0,row=4)
btn_deletr.grid(column=1,row=4)
btn_obter.grid(column=2,row=4)

#tv.insert("","end",values=(id,nome,fone))

app.mainloop()