from tkinter import *
# IMPORTANDO TUDO DO Tkinter

telaApp=Tk()

telaApp.title("CFB Cursos")
telaApp.geometry("1200x500")
telaApp.configure(background="#008")

txt1=Label(telaApp, text="Curso de Python", background="#FF0", foreground="#000")
txt1.place(x=10,y=10,width=150,height=30)

vtxt="Módulo Tkinter"
vgb="#ff0"
vfg="#000"
txt2=Label(telaApp,text=vtxt,bg=vgb,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X, expand=True)

telaApp.mainloop()