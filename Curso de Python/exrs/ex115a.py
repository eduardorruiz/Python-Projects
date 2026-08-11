"""Exercício Python 115a: Vamos criar um menu em Python, usando modularização."""
from Módulos.ex115 import *
from time import sleep

OK = False
while not OK:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('OP 1')
    elif resposta == 2:
        cabeçalho('OP 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        OK = True
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)