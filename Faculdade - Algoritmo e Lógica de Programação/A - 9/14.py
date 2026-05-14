"""Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida o
programa deve juntar as duas listas em uma única lista com o tamanho 20. """
l1 = []
l2 = []
for c in range(0, 10):
    n1 = int(input(f'Digite o {c}º valor de L1: '))
    l1.append(n1)
for c in range(0, 10):
    n2 = int(input(f'Digite o {c}ª valor de L2: '))
    l2.append(n2)
l3 = l1[:] + l2[:]
print(f'A L1 digitada foi {l1}')
print(f'A L2 digitada foi {l2}')
print('Agora L3, vai ser l1 + l2.')
print(f'A L3 é: {l3}')