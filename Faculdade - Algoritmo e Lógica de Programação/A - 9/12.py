"""Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros digitados pelo
usuário. Exiba na tela a lista preenchida. Em seguida, o programa deve procurar e eliminar os elementos que
eventualmente estiverem repetidos deixando apenas a primeira ocorrência de cada valor. Apresentar a lista
resultante na tela."""

N = int(input('Digite quantos elementos terá na lista: '))
cont = cont2 = 0
lista = []
while cont < N:
    valor = int(input(f'Digite {cont}° valor: '))
    if valor not in lista:
        lista.append(valor)
        print('adicionando...')
        print(lista)
    cont += 1
print(f'A lista completamente preenchida foi: {lista}')
lugares = []
for valor in lista:
    contador = lista.count(valor)

#Falta procurar os repetidos e exclui-los!