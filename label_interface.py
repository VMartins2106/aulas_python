from tkinter import *
from tkinter import messagebox

def mostrarMsg():
    messagebox.showinfo(title="CFB Cursos", message="CFB Cursos, curso de Python/Tkinter")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vnum_texto=StringVar()

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
#VALORES POSSÍVEIS PARA O 'RELIEF'
# FLAT (normal) / RAISED (3d elevada) / SUNKEN (funda) / SOLID (sem efeito)
fr_quadro1.place(x=10,y=10,width=300,height=100)

lb_tipo = Label(fr_quadro1,text="Tipo de messageBox(1,2 ou 3)")
lb_tipo.place(x=10,y=10)
tb_num=Entry(fr_quadro1,textvariable=vnum_texto)
vnum_texto.set("1")
tb_num.place(x=10,y=32)

btn_msg=Button(fr_quadro1,text="Mostrar mensagem", command=mostrarMsg)
btn_msg.place(x=10,y=60)

fr_quadro2 = Frame(app, borderwidth=1, relief="solid",background="#008") 
fr_quadro2.place(x=10,y=120,width=300,height=100)

# O QUE COLOCA ALGO DENTRO DE UM FRAME É O PRIMEIRO PARÂMETRO DEFINIDO PELO WIDGET

# CONTEÚDO NOVO - LABLE

# FORMATAÇÃO DE UMA LABLE:

lb_canal = Label(fr_quadro2,text="CFB Cursos", background="#008", foreground="#fff", font=("Arial",25))
lb_canal.pack(side=LEFT, fill=X, expand=True)

app.mainloop()