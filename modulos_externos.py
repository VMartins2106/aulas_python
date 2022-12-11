import modulos_externos_classe as classe

classe.canal_nome()
print(classe.jogador["nome"])

# IMPORTANDO ALGO DE OUTRA CLASSE APENAS IMPORTANDO-A

# IMPORTANDO APENAS O 'JOGADOR' DA CLASSE EM QUESTÃO

from modulos_externos_classe import jogador

res=dir(classe) # ESTE COMANDO CONSEGUE LER TUDO QUE TEM NA OUTRA CLASSE

print(res)
print(jogador["nome"])