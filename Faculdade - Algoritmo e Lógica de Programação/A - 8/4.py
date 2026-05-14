"""  Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida
o programa deve juntar as duas listas em uma única com o tamanho 20. """
cont = cont2 = 1
lista = []
lista2 = []
for c in range(0, 10):
    num = int(input(f'Digite o {cont}° valor da primeira lista: '))
    lista.append(num)
    cont += 1
print(f'A primeira lista é {lista}')
print('Agora digite os valores pra segunda lista, porfavor.')
for c in range(0, 10):
    num = int(input(f'Digite o {cont2}° valor da segunda lista: '))
    lista2.append(num)
    cont2 += 1
print('Você terminou de digitar ambas as listas.')
print('Muito obrigado, as duas listas juntas, encontram-se abaixo:')
lista3 = lista[:] + lista2[:]
print(lista3)