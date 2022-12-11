from tkinter import *

def futebolClicado():
    print("Futebol: " + str(vfut.get()))

def voleiClicado():
    print("Vôlei: " + str(vvol.get()))

def basqueteClicado():
    print("Basquete: " + str(vbas.get()))

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vfut=IntVar()
vvol=IntVar()
vbas=IntVar()

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
fr_quadro1.place(x=10,y=10,width=300,height=100)

cb_futebol=Checkbutton(fr_quadro1,text="Futebol",variable=vfut,onvalue=1,offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei=Checkbutton(fr_quadro1,text="Vôlei",variable=vvol,onvalue=1,offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete=Checkbutton(fr_quadro1,text="Basquete",variable=vbas,onvalue=1,offvalue=0, command=basqueteClicado)
cb_basquete.pack(side=LEFT)

app.mainloop()