soma = 0
contador = 0
for list in range(1, 501 , 2):
    if list % 3 == 0:
        soma = soma + list # ACUMULADOR e poderia ficar soma += list
        contador += 1
print(f'A soma de todos os {contador} valores solicitados é de {soma}')
