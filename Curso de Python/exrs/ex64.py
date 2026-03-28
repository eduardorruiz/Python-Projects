"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
 a soma entre eles (desconsiderando o flag)."""

n = int(input('Digite um número [999 para parar]: '))
cont = soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma foi de {soma}')