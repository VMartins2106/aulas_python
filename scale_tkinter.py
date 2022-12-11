from tkinter import *

def valorEscala():
    print("Valor da escala: " + str(sc_escala.get()))

def definirEscala():
    tamanho=lb_tamanho.get()
    sc_escala.set(int(tamanho))

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

lb_valor=Label(app,text="Valor")
lb_valor.pack()

sc_escala = Scale(app,from_=0,to=100,orient=HORIZONTAL)
sc_escala.set(0)
sc_escala.pack()

btn_valor=Button(app,text="Valor escala", command=valorEscala)
btn_valor.pack()

lb_valor=Label(app,text="Escolha um valor pra setar a scale: ")
lb_valor.pack()

lb_tamanho=Entry(app,text="Definir escala")
lb_tamanho.pack()

definir_escala=Button(app,text="Definir escala",command=definirEscala)
definir_escala.pack()



app.mainloop()