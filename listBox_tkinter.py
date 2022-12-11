from tkinter import *

def impEsp():
    print("Esporte selecionado: " + str(lb_esportes.get(ACTIVE)))

def addEsp():
    lb_esportes.insert(END,vnovoEsporte.get())
    vnovoEsporte.delete(0,END)

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

listaEsportes=["Futebol","Vôlei","Basquete"]

lb_esportes=Listbox(app)

for esportes in listaEsportes:
    lb_esportes.insert(END,esportes)

lb_esportes.pack()

btn_esporte=Button(app,text="Imprimir esporte", command=impEsp)
btn_esporte.pack()

lb_novo=Label(app,text="Inserir esportes")
lb_novo.pack()

vnovoEsporte=Entry(app)
vnovoEsporte.pack()

btn_inserir_esporte=Button(app,text="Adicionar esporte", command=addEsp)
btn_inserir_esporte.pack()

app.mainloop()