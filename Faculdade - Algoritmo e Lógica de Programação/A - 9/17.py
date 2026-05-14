
"""Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominados
A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam
aceitos valores repetidos. Em seguida, o programa deve juntar as duas listas em um única lista R (resultante)
tomando o cuidado de que a lista R não deve ter valores duplicados, EX:
nA = 5 --> A 16 8 25 12 19
nB = 7 --> B 5 14 3 27 8 21 44
nR = 11 --> R 16 8 25 12 19 5 14 3 27 21 44 (note que o valor 8 da lista B não foi incluído na lista resultante)"""

A = []
B = []
R = []
na = int(input('Digite quantos elementos terá a lista A (nA): '))
nb = int(input('Digite quantos elementos terá a lista B (nB): '))
print('- -' * 14)
for c in range(na):
    valor = int(input(f'Digite o {c + 1}º valor da lista A: '))
    A.append(valor)
    R.append(valor)
print('- -' * 14)
for c in range(nb):
    valor = int(input(f'Digite o {c + 1}º valor da lista B: '))
    B.append(valor)
    if valor not in R:
        R.append(valor)
print('- -' * 14)
print(f'A lista resultante é: {R}')
