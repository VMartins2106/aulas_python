from tkinter import *
import os

# GIF's SÃO EXTENSÕES DE IMAGENS QUE RODAM E FUNCIONAM MUITO BEM NO TKINTER
pastaApp=os.path.dirname(__file__)

app=Tk()
app.title("CFB Cursos")
app.geometry("500x500")

imgGIF=PhotoImage(file=pastaApp+"\\ney.gif")
# SEGREDO PRA FUCNIONAR É COLOCAR O PACK/PLACE DA IMAGEM EM UM LABLE

lb_gif=Label(app,image=imgGIF)
lb_gif.place(x=10,y=10)

app.mainloop()