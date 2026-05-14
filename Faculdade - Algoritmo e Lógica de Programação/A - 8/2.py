""" Refaça o programa anterior, porém ao final exiba na tela cada elemento da lista em uma linha da tela
(este programa deve exibir um elemento por vez dentro de um laço e usando um índice para acessar
cada elemento individualmente). """

num = int(input('Digite o primeiro valor: '))
lista = []
if num > 0:
    lista.append(num)
while num > 0:
    num = int(input('Digite mais um valor: '))
    if num > 0:
        lista.append(num)
for valores in lista:
    print(valores)