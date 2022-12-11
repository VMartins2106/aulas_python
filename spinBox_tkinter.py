from tkinter import *

def impValor():
    print("Valor escolhido: " + str(spin_valores.get()))

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

# spin_valores=Spinbox(app,from_=0,to=10)
# TAMBÉM FUNCIONA ASSIM:
spin_valores=Spinbox(app,values=(1,2,3,4,5))
# SET FUNCIONA PARA SETAR DE FORA DO SPINBOX
spin_valores.pack()

btn_valor=Button(app,text="Imprimir valor",command=impValor)
btn_valor.pack()

app.mainloop()