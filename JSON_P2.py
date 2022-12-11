import json

carros_dictionary={
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
# DICTIONARY --> OBJETO JSON

carros_list=["honda","volkswagem", "ford", "fiat", "chevrolet"]
# list --> array json

carros_tupla=("honda","volkswagem", "ford", "fiat", "chevrolet")
# tupla --> array json

# DIFERENTES VARIAVEIS VIRAM DIFERENTES SAIDAS JSON

carros_json_dict=json.dumps(carros_dictionary) # ESTE VIRA UM --> OBJETO
carros_json_list=json.dumps(carros_list)  # ESTE VIRA A MESMA COISA DO POSTERIOR -> ARRAY
carros_json_tupla=json.dumps(carros_tupla) # ESTE VIRA A MESMA COISA DO ANTERIOR  -> ARRAY

# ESTILIZANDO O DICT EM JSON
carros_json_dict=json.dumps(carros_dictionary, indent=4, separators=(":", "="),sort_keys=True)
# INDENT DÁ ESPAÇO ANTES DO QUE ESTIVER ESCRITO
# SEPARATORS ALTERA O QUE SEPARA A KEY DO VALUE
# SORT_KEYS ALTERA E COLOCA OS ELEMENTOS EM ORDEM ALFABÉTICA

print(carros_json_dict)