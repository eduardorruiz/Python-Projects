""" Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar."""
from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
Ano_de_nascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - Ano_de_nascimento
pessoa['Carteira_de_trabalho'] = int(input('Carteira de trabalho(0 se não tem): '))
if pessoa['Carteira_de_trabalho'] != 0:
    pessoa['Ano_de_contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Idade_de_aposentadoria'] = ((pessoa['Ano_de_contratação'] + 35) - datetime.now().year) + pessoa['Idade']
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor [ {v} ].')
    print('- - - ' * 10)
