''' Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário. '''

print('Todos os valores inteiros divisíveis por 5 entre um número mínimo e um máximo')
min = int(input('Digite o valor mínimo: '))
max = int(input('Digite o valor máximo: '))
num = min
if min > max:
    print(' ERROR')
else:
    while num <= max:
        if num % 5 == 0:
            print(num)
        num += 1
print('\nFim do Programa')