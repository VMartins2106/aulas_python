
# HERANÇA DE CLASSES

class NPC: #BASE, PAI, SUPER
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome......: " + self.nome)
        print("Time......: " + str(self.time))
        print("Força.....: " + str(self.forca))
        print("Munição...: " + str(self.municao))
        print("Vivo......: " + ("Sim" if self.vivo else "Não"))
        print("Energia...: " + str(self.energia))
        print("----------------------------------------------")

class Soladado(NPC): # CLASSE FILHO 1
    def __init__(self,nome,time):
        self.forca=200
        self.municao=200
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()

class Guarda(NPC): # CLASSE FILHO 2
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()

class Elite(NPC): # CLASSE FILHO 3
    def __init__(self,nome,time):
        self.forca=400
        self.municao=500
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()

s1=Guarda("Olho vivo", 1)
s2=Soladado("Bala na agulha", 1)
s3=Elite("Ninja", 1)
s4=Guarda("Super atento", 2)
s5=Soladado("Tiro certo", 2)
s6=Elite("Samurai", 2)

s1.vivo=False
s6.vivo=False

s1.inf()
s2.inf()
s3.inf()
s4.inf()
s5.inf()
s6.inf()