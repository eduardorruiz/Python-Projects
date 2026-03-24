''' Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo
usuário, a quantidade de valores, a soma e a média de todos. '''
print('-=-' * 22)
print('Esse programa mostra o maior e menor valores informados pelo \nusuário, a quantidade de valores, a soma e a média de todos.')
print('-=-' * 22)
n = int(input('Digite um número: '))
cont = soma = 0
menor = maior = n
while n > 0:
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    n = int(input('Digite mais um número: '))
media = soma / cont
print('O maior número informado foi [{}] e o menor foi [{}].'.format(maior, menor))
print('A quantidade de valores válidos informados foi de [{}].'.format(cont))
print('A soma de todos os valores informados foi de [{}].'.format(soma))
print('A média de todos os valores informados foi de [{}].'.format(media))
