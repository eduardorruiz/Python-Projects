""" Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""
dados = {}
lista = list()
dados['nome'] = str(input('Digite seu nome: ')).strip()
média = float(input('Digite sua média: '))
dados['média'] = média
if média > 6:
    dados['Situação'] = 'APROVADO'
else:
    dados['Situação'] = 'de RECUPERAÇÃO'
print(dados)
lista.append(dados.copy())
print(f'O aluno {dados['nome']}, tem a média {dados['média']} e está {dados['Situação']}')