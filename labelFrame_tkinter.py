from tkinter import *

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

lb_esportes=LabelFrame(app,text="Esportes", borderwidth=1,relief="solid")
lb_esportes.place(x=10,y=10,width=300,height=100)

le1=Label(lb_esportes,text="Futebol")
le1.place(x=10,y=10)

le2=Label(lb_esportes,text="Vôlei")
le2.place(x=10,y=30)

le3=Label(lb_esportes,text="Basquete")
le3.place(x=10,y=50)

app.mainloop()