import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters+s.digits+s.punctuation,k=12)))

# DIGITS = TODOS OS DIGITOS
# ASCII_LETTERS = LETRAS MAIUSCULAS E MINUSCULAS
# PUNCTUATION = PONTUAÇÕES
# K É O TAMANHO DA SENHA