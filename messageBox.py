from tkinter import *
from tkinter import messagebox

def mostrarMsg(tiposMsg, msg):
    if tiposMsg == "1":
        messagebox.showinfo(title="CFB Cursos", message=msg)
    elif tiposMsg == "2":
        messagebox.showwarning(title="CFB Cursos", message=msg)
    elif tiposMsg == "3":
        messagebox.showerror(title="CFB Cursos", message=msg)

def resetarTextBox():
    res=messagebox.askyesno("Resetar","Confirmar reset do text box ?")
    # ASK YES NO / ASK QUESTION -> TRAZ SIM E NÃO, RETORNANDO TRUE OU FALSE
    # ASK OK CANCEL -> TRAZ SIM E CANCELAR, RETORNANDO TRUE OU FALSE
    # ASK RETRY CANCEL -> TRAZ REPETIR E CANCELAR, RETORANDO TRUE OU FALSE
    # ASK YES NO CANCAL -> TRAZ SIM, NÃO E CANCELAR, RETORNANDO TRUE, FALSE OU NONE
    if res == True:
        tb_num.delete(0,END)
        tb_num.insert(0,"1")

vmsg="Curso de python/tkinter"

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vnum_texto=StringVar()

Label(app,text="Tipo de messageBox(1,2 ou 3)").pack()
tb_num=Entry(app,textvariable=vnum_texto)
vnum_texto.set("1")
tb_num.pack()

btn_msg=Button(app,text="Mostrar mensagem", command=lambda:mostrarMsg(vnum_texto.get(), vmsg))
btn_msg.pack()

btn_reset=Button(app,text="Resetar textBox", command=resetarTextBox)
btn_reset.pack()


app.mainloop()