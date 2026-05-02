"""Aprimore o desafio anterior, mostrando no final
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somaterceiracoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        if matriz[linha][2]:
            somaterceiracoluna += matriz[linha][coluna]
print('-~' * 16)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end = '')
    print()
print('-~' * 16)
print(f'A soma de todos os valores pares digitados foi [{somapares}].')
print('--' * 28)
print(f'A soma dos valores da terceira coluna foi [{somaterceiracoluna}].')
print('--' * 28)
print(f'O maior valor da segunda linha foi [{max(matriz[1])}].')
print('-~' * 16)
print('\nFim do Programa')
