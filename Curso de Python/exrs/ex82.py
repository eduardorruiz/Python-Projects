""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

lista = []
par = []
impar = []
stop = 'S'
while stop != 'S' and stop != 'N':
    stop = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
while stop == 'S':
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
        print('Esse valor foi adicionado na lista dos pares.')
    else:
        impar.append(n)
        print('Esse valor foi adicionado na lista dos ímpares.')
    stop = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'A lista total é {lista}')
print(f'A lista dos pares é {par}')
print(f'A lista dos ímpares é {impar}')