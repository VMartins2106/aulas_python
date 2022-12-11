import json

carros_json = '{"marca": "honra","modelo": "HRV","cor": "prata"}' # EM JSON

carros_py={"marca": "honra","modelo": "HRV","cor": "prata"} # DICT EM PYTHON    

#CONVERTER DICT DE PYTHON EM JSON:
carros_em_python=json.dumps(carros_py)

#SUBINDO ARQUIVO JSON EM JSON:
carros_em_json=json.loads(carros_json)

# IMPRIME TUDO NORMALMENTE
print(carros_em_json)
print(carros_em_python)

# CRIAMOS UM ARQUVIO CARROS EM JSON E CARREGAMOS ELE EM JSON PRA OUTRA VARIÁVEL
# ALTERAÇÃO E IMPRESSÃO DE 'CARROS', EM JSON, É A MESMA QUE EM UM DICT NORMAL

print(carros_em_json["modelo"])

for x in carros_em_json:
    print(x)

for x in carros_em_json.values():
    print(x)

for k,v in carros_em_json.items():
    print(k,v)

# ATÉ AGORA TUDO IGUAL AO DICT