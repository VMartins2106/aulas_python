from tkinter import *
import os
import banco

print(x)

def gravarDados():
    nome = nomezao.get()
    if nome != "":
        vnome=nomezao.get()
        vfone=tb_fone.get()
        vemail=tb_email.get()
        vobs=tb_obs.get("1.0", END)
        vquery="INSERT INTO tb_menu (nomeMenu,telefoneMenu,emailMenu,obsMenu) VALUES ('"+vnome+"','"+vfone+"','"+vemail+"','"+vobs+"')"
        banco.dml(vquery)
        nomezao.delete(0,END)
        tb_fone.delete(0,END)
        tb_email.delete(0,END)
        tb_obs.delete("1.0",END)
        print("Dados gravados")
    else:
        print("ERRO")

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
nomezao=Entry(telaApp)
nomezao.place(x=10,y=30,width=200,height=20)

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
tb_fone=Entry(telaApp)
tb_fone.place(x=10,y=80,width=100,height=20)

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
tb_email=Entry(telaApp)
tb_email.place(x=10,y=130,width=300,height=20)

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
tb_obs=Text(telaApp)
tb_obs.place(x=10,y=180,width=300,height=80)

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