from tkinter import *
from tkinter import ttk

def imprimirEsporte():
    vesporte=cb_esportes.get()
    print("Esporte selecionado: " + vesporte)

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

listaEsportes = ["Futebol", "Vôlei", "Basquete"] # LISTA PARA PASSAR OPÇÕES DA COMBO BOX

lb_esportes=Label(app,text="Esportes")
lb_esportes.pack()

cb_esportes = ttk.Combobox(app,values=listaEsportes) # 'TTK' IMPORTA O COMBOBOX E MUITO MAIS
cb_esportes.set("Futebol") # COMEÇA COM ISTO SELECIONADO, MAS PODE ESTAR VAZIO TAMBÉM
cb_esportes.pack()

btn_esporte=Button(app,text="Esporte selecionado",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()