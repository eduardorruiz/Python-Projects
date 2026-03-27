""" Reescreva um programa do exercício acima considerando exclusivamente os números positivos
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
"número inválido" e o valor deve ser ignorado. """

n = int(input('N: '))

primvalorOK = False #flag
cont = 0
while cont < n:
    x = float(input(f'Digite o elemento {cont + 1}: '))
    if x <= 0:
        print('Valor invalido')
    else:
        if  not primvalorOK and x > 0:
            maior = menor = x
            primvalorOK = True
        else:
            if x > maior:
                maior = x
            if x < menor:
                menor = x
            cont += 1 # se tiver dentro do segundo else

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')


