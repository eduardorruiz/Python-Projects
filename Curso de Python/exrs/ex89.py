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
    nome = str(input('Nome: ')).capitalize().strip()
    temporaria.append(nome)
    nota1 = float(input('Nota 1: '))
    temporaria.append(nota1)
    nota2 = float(input('Nota 2: '))
    temporaria.append(nota2)
    media = (nota1 + nota2) / 2
    media = int(media)
    temporaria.append(media)
    lista.append(temporaria[:])
    temporaria.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('ERRO, Quer continuar [S/N]? ')).strip().upper()[0]
    print('--' * 13)

"""for i, pessoa in enumerate(lista):
    print(f'Aluno {i}: {pessoa[i][0]:^10} | [{pessoa[i][3]:^5}].')"""
#print(lista)
print('\nFim do Programa')