print('{:-^50}'.format(' Programa de Soma de Pares '))
soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print(f'A soma dos números pares apresentados acima foi de {soma} e tiveram {cont} números pares informados.')
