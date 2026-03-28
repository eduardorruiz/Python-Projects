maior = 0
menor = 0
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}° pessoa, em kg: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso lido foi de {p} kg.')
print(f'O menor peso lido foi de {menor} kg.')