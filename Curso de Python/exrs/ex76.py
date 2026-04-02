""" Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Reguá', 9,
            'Caderno', 15,
            'Estojo', 10,
            'Transferidor', 10,
            'Mochila', 99)
print('-'*30)
print(f'{"Listagem de produtos":^30}')
print('-'*30)
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<20}', end = '')
    else:
        print(f'R${listagem[posição]:>6.2f}')