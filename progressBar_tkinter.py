from tkinter import *
from tkinter import ttk

def valorBarra(m):
    cont=0
    etapas=m/100
    while cont<etapas:
        cont+=1
        i=0
        while i<1000000:
            i+=1
        varBarra.set(cont)
        app.update() # ATUALIZA A TELA PARA TER PROGRESSO EM TEMPO REAL

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

varBarra=DoubleVar()
varBarra.set(0) # AQUI INICIA O PROGRESSO DA BARRA

pb=ttk.Progressbar(app,variable=varBarra,maximum=100) # AQUI DEFINE ELA E FALA O SEU VALOR MÁXIMO
pb.place(x=0,y=0,width=500,height=40)

btn=Button(app,text="Definir barra", command=lambda:valorBarra(10000))
btn.place(x=0,y=50,width=100,height=40)

app.mainloop()