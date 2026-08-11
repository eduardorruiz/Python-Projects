"""Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python."""
from Módulos.ex115.interface import *
from Módulos.ex115.arquivo import *
from time import sleep

arq = 'ex115arquivo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
OK = False
while not OK:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('OP 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        OK = True
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)