""" Escreva um programa que leia uma lista com N números inteiros, onde N é um número inteiro previamente
digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que
quando esta situação ocorrer uma mensagem deve ser dada ao usuário. Por fim exibir na tela a lista resultante."""
list = []
N = int(input('Digite a quantidade de elementos da sua lista: '))
for c in range(N):
    num = int(input(f'Digite o {c + 1}º valor da lista: '))
    if num not in list:
        list.append(num)
        print('Adicionando...')
    else:
        print('Esse valor já está na lista.\nPortanto, não será adicionado.')
print(f'A lista resultante é {list}')
