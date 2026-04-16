""" Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista = []
menor = maior = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a {c + 1}ª posição: ')))
    if c == 0:
        maior = menor = lista[0]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=-' * 20)
print(f'A lista digitada foi {lista}')
print(f'O menor valor da lista foi [{menor}], e foi encontrado na posição ', end='')
for posição, valor in enumerate(lista):
    if valor == menor:
        print(f'{posição + 1}...', end='')
print()
print(f'O maior valor da lista foi [{maior}], e foi encotrado na posição', end='')
for posição, valor in enumerate(lista):
    if valor == maior:
        print(f'{posição + 1}...', end='')
print()
print('\n\nFim do Programa')