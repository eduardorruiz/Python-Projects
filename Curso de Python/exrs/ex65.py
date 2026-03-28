"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da
execução,mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

n = int(input('Digite um número: '))
parada = str(input('Deseja continuar [S/N]: ')).upper()
contador = 1
soma = media = 0
while parada != 'N':
    media = soma / contador
    soma += n
    contador += 1
    n = int(input('Digite um número: '))
    parada = str(input('Deseja continuar [S/N]: ')).upper()
print(f'Você digitou {contador} números e a média foi de {media:.2f}')