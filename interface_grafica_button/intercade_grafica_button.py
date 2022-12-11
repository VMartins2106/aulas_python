from tkinter import *
import os

c=os.path.dirname(__file__)
nomeArquivo=c+"\\dados.txt"

def gravarDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("Nome.......:%s" % vnome.get())
    arquivo.write("\nTelefone...:%s" % vfone.get())
    arquivo.write("\nEmail......:%s" % vemail.get())
    arquivo.write("\nOBS........:%s" % vobs.get("1.0", END))
    arquivo.write("\n")
    arquivo.close()

telaApp=Tk()

telaApp.title("CFB Cursos")
telaApp.geometry("500x300")
telaApp.configure(background="#dde")

# ANCORA : N (NORTE), S (SUL), E (LESTE), W (OESTE) --> PODEM SER COMBINADOS:
# NE (NOROESTE) SE (SUDESTE) SO (SUDOESTE) NO (NOROESTE)
Label(
    telaApp, 
    text="Nome: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=10,
        width=100,
        height=20
    )
vnome=Entry(telaApp)
vnome.place(x=10,y=30,width=200,height=20)

Label(
    telaApp, 
    text="Telefone: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=60,
        width=100,
        height=20
    )
vfone=Entry(telaApp)
vfone.place(x=10,y=80,width=100,height=20)

Label(
    telaApp, 
    text="Email: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=110,
        width=100,
        height=20
    )
vemail=Entry(telaApp)
vemail.place(x=10,y=130,width=300,height=20)

Label(
    telaApp, 
    text="OBS: ",
    background="#dde", 
    foreground="#009", 
    anchor=W).place(
        x=10,
        y=160,
        width=100,
        height=20
    )
vobs=Text(telaApp)
vobs.place(x=10,y=180,width=300,height=80)

Button(
    telaApp, 
    text="Gravar",
    command=gravarDados
    ).place(
        x=10,
        y=270,
        width=100,
        height=20
        )
    

telaApp.mainloop()