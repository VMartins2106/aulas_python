import datetime

nasc = datetime.datetime.now()
#data pronta
dataa = datetime.datetime(1985,3,7) # CRIANDO DATA PRONTA

print(str(dataa.day) + " / " + str(dataa.month) + " / " + str(dataa.year))

print(nasc.strftime("%a")) # DESCOBRINDO O DIA DA SEMANA ABREVIADO (TEXTO)
print(nasc.strftime("%A")) # DESCOBRINDO O DIA DA SEMANA (TEXTO)
print(nasc.strftime("%w")) # DESCOBRINDO O DIA (numero) DA SEMANA RELATIVO A ...-feira
print(nasc.strftime("%d")) # DESCORBINDO O DIA (numero) DO MÊS
print(nasc.strftime("%b")) # DESCOBRINDO O MES (TEXTO) ABREVIADO
print(nasc.strftime("%B")) # DESCOBRINDO O MES (TEXTO) 
print(nasc.strftime("%m")) # DESCOBRINDO O DIA DO MES (NUMERO)
print(nasc.strftime("%y")) # DESCOBRINDO O ANO COM 2 DIGITOS
print(nasc.strftime("%Y")) # DESCOBRINDO O ANO COM 4 DIGITOS
print(nasc.strftime("%H")) # DESCOBRINDO A HORA COM 2 DIGITOS (00:00-23:00)
print(nasc.strftime("%I")) # DESCOBRINDO A HORA COM TODOS OS DIGITOS (00:00 - 12:00)
print(nasc.strftime("%p")) # DESCOBRINDO SE É MANHÃ OU TARDE
print(nasc.strftime("%M")) # DESCOBRINDO OS MINUTOS
print(nasc.strftime("%S")) # DESCOBRINDO OS SEGUNDOS
print(nasc.strftime("%f")) # DESCOBRINDO OS MICROSEGUNDOS
print(nasc.strftime("%j")) # DESCOBRINDO O DIA DO ANO (ATÉ 365)
print(nasc.strftime("%W")) # DESCOBRIDNO A SEMANA DO ANO

# FUNÇÕES COM DATA