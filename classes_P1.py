
# EXEMPLOS E REGRAS SOBRE CLASSES

class Carro:
    velMax=0
    ligado=False
    cor=""

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax=200
c1.cor="preto"
c1.ligado=False

c2.velMax=100
c2.cor="cinza"
c2.ligado=True

c3.velMax=600
c3.cor="azul"
c3.ligado=False

print("Velocidade máxima: " + str(c1.velMax))
print("Cor: " + str(c1.cor))
estado="Sim" if c1.ligado else "Não"
print("Ligado: " + estado)

print("\n")

print("Velocidade máxima: " + str(c2.velMax))
print("Cor: " + str(c2.cor))
estado="Sim" if c2.ligado else "Não"
print("Ligado: " + estado)

print("\n")

print("Velocidade máxima: " + str(c3.velMax))
print("Cor: " + str(c3.cor))
estado="Sim" if c3.ligado else "Não"
print("Ligado: " + estado)