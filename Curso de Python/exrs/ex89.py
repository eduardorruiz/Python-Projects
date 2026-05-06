""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
# lista = [[nomeX, nota1X, nota2X, mediaX], [nomeY, nota1Y, nota2y, mediaY], ... ]
# nome = 0, nt1 = 1, nt2 = 2, media = 3, (SE QUISER COLOCAR) indice = 4
lista = list()
temporaria = list()
resposta = 'S'
print('-' * 30)
print('{:*^30}'.format(' PROGRAMA DE BOLETIM '))

print('-' * 30)
while resposta == 'S':
    # poderia adicionar tudo com temporaria.append([nome], [nota1, nota2], media])
    nome = str(input('Nome: ')).capitalize().strip()
    temporaria.append(nome)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    temporaria.append([nota1, nota2])
    media = (nota1 + nota2) / 2
    temporaria.append(media)
    lista.append(temporaria[:])
    temporaria.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('ERRO, Quer continuar [S/N]? ')).strip().upper()[0]
    print('--' * 13)
for i, a in enumerate(lista):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
    print('--' * 13)
resp = str(input('Deseja ver as notas de algum aluno [S/N]: ')).strip().upper()[0]
while resp == 'S':
    opcao = int(input('Digite o índice do aluno, que deseja ver as notas: '))
    opcao = opcao - 1
    if opcao > -1:
        if opcao <= len(lista) - 1:
            print(f'Notas de {lista[opcao][0]} são {lista[opcao][1]}')
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('ERRO, Quer continuar [S/N]: ')).strip().upper()[0]
print('\nFim do Programa')