n1=10
n2=5

def somar():
    r=n1+n2
    print("A soma de " + str(n1) + " e " + str(n2) + " é igual a: " + str(r))

def subtrair():
    r=n1-n2
    print("A subtração de " + str(n1) + " e " + str(n2) + " é igual a: " + str(r))

def multiplicar():
    r=n1*n2
    print("A multiplicação de " + str(n1) + " e " + str(n2) + " é igual a: " + str(r))

def dividir():
    r=n1/n2
    print("A divisão de " + str(n1) + " e " + str(n2) + " é igual a: " + str(r))

def calculos():
    somar()
    subtrair()
    multiplicar()
    dividir()

calculos()