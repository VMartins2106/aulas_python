from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pastaApp = os.path.dirname(__file__)

def mp(mm):
    return mm/0.351777

def criarPDF():
    try:
        cnv=canvas.Canvas(pastaApp+"\\cfbcursos.pdf",pagesize=A4)
        cnv.drawImage(pastaApp+"\\ramon.jpg",mp(50),mp(200))
        cnv.circle(mp(115),mp(100),mp(25))
        cnv.drawString(mp(100),mp(100),"CBF CURSOS")
        cnv.save()
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao criar arquivo PDF")
        return
    messagebox.showinfo(title="PDF", message="PDF criado")

app=Tk()
app.title("CFB Cursos")
app.geometry("600x450")

btn_criarPDF=Button(app,text="Criar PDF", command=criarPDF)
btn_criarPDF.pack(pady=20)

app.mainloop()