""" Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do
Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores."""
from time import sleep
resp = 's'
while resp != 'fim':
    print('-'*30)
    print('SISTEMA DE AJUDA PYTHON')
    print('-'*30)
    sleep(0.8)
    resp = str(input('Biblioteca ou função: ')).strip().lower()
    print('-' * 30)
    print()
    if resp != 'fim':
        resp = str(resp)
        help(resp)
    else:
        print('Programa finalizado com sucesso!')

# FALTA COLOCAR AS CORES!!!!