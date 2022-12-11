from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

def semComando():
    print("")

def novoContato():
    exec(open(pastaApp+"\\novo_contato.py").read(),{'x':10})

telaApp=Tk()

telaApp.title("CFB Cursos")
telaApp.geometry("500x300")
telaApp.configure(background="#dde")

barraDeMenus=Menu(telaApp)
menuContatos=Menu(barraDeMenus,tearoff=0)
menuContatos.add_command(label="Novo", command=novoContato)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=telaApp.quit)
barraDeMenus.add_cascade(label="Contatos",menu=menuContatos)

menuManutencao=Menu(barraDeMenus,tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção",menu=menuManutencao)

menuSobre=Menu(barraDeMenus,tearoff=0)
menuSobre.add_command(label="CFB Cursos", command=semComando)
barraDeMenus.add_cascade(label="Sobre",menu=menuSobre)

telaApp.config(menu=barraDeMenus)

telaApp.mainloop()