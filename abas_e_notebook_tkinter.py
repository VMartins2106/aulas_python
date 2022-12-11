from tkinter import *
from tkinter import ttk

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

nb=ttk.Notebook(app)
nb.place(x=0,y=0,width=500,height=300)

tb1 = Frame(nb)
tb2= Frame(nb)
tb3 = Frame(nb)
tb4 = Frame(nb)
tb5 = Frame(nb)
nb.add(tb1,text="HTML")
nb.add(tb2,text="C#")
nb.add(tb3,text="Python")
nb.add(tb4,text="REACT")
nb.add(tb5,text="Dart")

# CADA LABLE EM UMA ABA (TB) DENTRO DO NOTEBOOK
lb1=Label(tb1,text="Curso de HTML")
lb1.pack()
lb2=Label(tb2,text="Curso de C#")
lb2.pack()
lb3=Label(tb3,text="Curso de Python")
lb3.pack()
lb4=Label(tb4,text="Curso de REACT")
lb4.pack()
lb5=Label(tb5,text="Curso de Dart")
lb5.pack()

app.mainloop()