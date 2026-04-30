""" Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. """
# Solução 1 - meio errada, mas funciona 100%
"""
numeros = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(numeros[:])
        pares.sort()
        numeros.clear()
    else:
        impares.append(numeros[:])
        impares.sort()
        numeros.clear()
print(f'- = -' * 10 )
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
"""

# Solução 2
numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
        numeros[0].sort()
    else:
        numeros[1].append(n)
        numeros[1].sort()
print(f'- = -' * 10 )
print(f'Os valores digitados foram: {numeros}')
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
