"""Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros digitados pelo
usuário. Exiba na tela a lista preenchida. Em seguida, o programa deve procurar e eliminar os elementos que
eventualmente estiverem repetidos deixando apenas a primeira ocorrência de cada valor. Apresentar a lista
resultante na tela."""

N = int(input('Digite quantos elementos terá na lista: '))
cont = cont2 = 0
lista = []
while cont < N:
    valor = int(input(f'Digite {cont}° valor: '))
    lista.append(valor)
    cont += 1
print(lista)

#Falta procurar os repetidos e exclui-los!