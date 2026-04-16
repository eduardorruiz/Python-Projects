""" Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente."""

lista = []
num = lista.append(int(input('Digite um valor: ')))
continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
while continuar == 'S':
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor digitado já está na lista, não vou adicionar...')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
lista.sort()
print(f'A lista digitada foi {lista}')
