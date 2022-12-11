import os

carros=[]

class Carro:
    nome=""
    potencia=0
    velMax=0
    ligado=False
    def __init__(self, nome,potencia):
        self.nome = nome
        self.potencia = potencia
        self.velMax = int(potencia*2)
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def info(self):
        print("Nome.......: " + self.nome)
        print("Potência...: " + str(self.potencia))
        print("Vel Máxima.: " + str(self.velMax))
        print("Ligado.....: " + ("Sim" if self.ligado==True else "Não"))

def menu():
    os.system('cls') or None
    print("1 - Novo carro")
    print("2 - Informações do carro")
    print("3 - Excluir carro")
    print("4 - Ligar carro")
    print("5 - Desligar carro")
    print("6 - listar carro")
    print("7 - Sair do programa")
    print("Quantidade de carros: " + str(len(carros)))
    op = input("Digite uma das opção: ")
    return op

def novoCarro():
    os.system('cls') or None
    n = input("Digite o nome do carro.......: ")
    p = input("Digite a potência do carro...: ")
    car = Carro(n,p)
    carros.append(car)
    print("Novo carro criado")
    os.system("pause")

def informacoesCarro():
    os.system('cls') or None
    n = input("Digite o número do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
        os.system("pause")
    except:
        print("Carro não existe na lista !")
        os.system("pause")

def excluirCarro():
    os.system('cls') or None
    n = input("Digite o número do carro que deseja excluir: ")
    try:
        del carros[int(n)]
    except:
        print("Carro não existe na lista !")
        os.system("pause")

def ligarCarro():
    os.system('cls') or None
    n = input("Digite o número do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro ligado")
    except:
        print("Carro não existe na lista !")
        os.system("pause")

def desligarCarro():
    os.system('cls') or None
    n = input("Digite o número do carro que deseja ligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("Carro não existe na lista !")
        os.system("pause")

def listarCarros():
    os.system('cls') or None
    p=0
    for c in carros:
        print(str(p) + " - " + c.nome)
        p=p+1
    os.system("pause")

ret = menu()
while ret<"7":
    if ret=="1":
        novoCarro()
    elif ret=="2":
        informacoesCarro()
    elif ret=="3":
        excluirCarro()
    elif ret=="4":
        ligarCarro()
    elif ret=="5":
        desligarCarro()
    elif ret=="6":
        listarCarros()
    ret=menu()

os.system('cls')
print("Programa finalizado.")
