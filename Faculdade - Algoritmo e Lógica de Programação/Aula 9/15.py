"""Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes
tamanhos nA e nB, respectivamente. Em seguida o programa deve juntar as duas listas em uma única lista com o
tamanho nA+nB. Exibir na tela a lista resultante. Veja o exemplo:
nA = 5 - A: 16 8 25 12 19
nB = 7 - B: 5 14 3 27 8 21 44
nR = 12 - R: 16 8 25 12 19 5 14 3 27 8 21 44"""
A = []
B = []
na = int(input('Digite quantos elementos terá a lista A (nA): '))
nb = int(input('Digite quantos elementos terá a lista B (nB): '))
print('- -' * 14)
while na == nb:
    print('Erro, os valor de nA e nB não podem ser iguais.')
    nb = int(input('Digite um novo valor para nB: '))
    print('- -' * 14)
for c in range(na):
    valor = int(input(f'Digite o {c}º valor da lista A: '))
    A.append(valor)
print('- -' * 14)
for c in range(nb):
    valor = int(input(f'Digite o {c}º valor da lista B: '))
    B.append(valor)
C = A[:] + B[:]
print('- -' * 14)
print(f'A quantidade de elementos na lista resultante (nC) é [{len(C)}].')
print(f'A soma das listas é: {C}')

